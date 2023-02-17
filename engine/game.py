from typing import AsyncGenerator, Generator, List, Optional, Tuple

import numpy as np

from engine.actions import Action
from engine.agents import BaseAgent
from engine.board import TetrisBoard
from engine.piece import TetrisPiece
from engine.pieces import PIECES


class TetrisGame:
    agent: BaseAgent
    seed: int
    score: int
    running: bool
    board: TetrisBoard

    def __init__(self, agent: BaseAgent, seed: int = -1) -> None:
        self.agent = agent
        self.seed = seed

        self.score = 0
        self.running = True
        self.board = TetrisBoard()

    def generate_pieces(self) -> Generator[TetrisPiece, None, None]:
        """Generates a list of all the pieces and yields them in order for the game.

        Args:
            curr_board (List[List[Optional[str]]]): The 2D list board state to compare to this object's.

        Yields:
            List[Tuple[str, int, int]]: List of changes in the form (cell value, y, x).
        """

        random_state = np.random.RandomState(None if self.seed == -1 else self.seed)
        pieces = random_state.randint(7, size=1000)  # type: ignore

        for piece in pieces:
            if not self.running:
                return

            yield PIECES[piece]()

    async def run(
        self,
    ) -> AsyncGenerator[
        Tuple[
            Optional[List[Tuple[str, int, int]]],
            Optional[List[int]],
            TetrisBoard,
            Optional[Action],
        ],
        None,
    ]:
        """Runs the Tetris game. The meat and potatoes of the Tetris engine.

        Yields: AsyncGenerator[
                    Tuple[Optional[Union[List[Tuple[str, int, int]], List[int]]],
                    int,
                    TetrisBoard,
                    Optional[Action]],
                    None
                ]:
                A list of changes to the board in the form (piece_type, y, x) or a list of the line indices cleared.
                The game's current score.
                The current state of the board object of this game.
                The action taken if any.
        """

        # Make a copy of the board at this point for comparision
        old_board = self.board.copy()

        for piece in self.generate_pieces():
            # Set the new piece to be the current one and spawn it
            self.board.set_piece(piece)
            if not self.board.spawn_piece():
                self.running = False
                if changes := self.board.get_changes(old_board):
                    yield changes, None, self.board, None

                return

            while not piece.landed:
                # Get board differences
                changes = self.board.get_changes(old_board)

                # This yield updates the new piece spawning
                yield changes, None, self.board, None

                # Wait for agent to make a move
                action = await self.agent.play_move(self.board)
                assert action in Action

                # Reset the previous board to the current
                old_board = self.board.copy()

                # Perform the action
                self.board.apply_action(action)

                # Yield the changes to the board once the current action has taken place
                # Deals with cases of repeated movement into corner or hard drop when just above another piece
                # Moves are yielded regardless so that they are still recorded
                changes = self.board.get_changes(old_board)
                yield changes, None, self.board, action

                if changes:
                    old_board = self.board.copy()

            # Get indices of lines to clear
            lines_to_clear = self.board.find_lines_to_clear()

            if lines_to_clear:
                # Clear the lines, yield the change, and reset previous board to current
                self.score += self.board.clear_lines(lines_to_clear)

                yield None, lines_to_clear, self.board, None
                old_board = self.board.copy()

            # Update the running state of the game
            self.running = self.board.is_game_running()

            # If the game is not running but there is one last change, yield it
            # In the case of a piece moving/rotating right at the end
            if not self.running and (changes := self.board.get_changes(old_board)):
                yield changes, None, self.board, None
