import random
from typing import AsyncGenerator, Generator, List, Optional, Tuple

from tetris.agent import BaseAgent
from tetris.board import Action, Board
from tetris.piece import Piece
from tetris.pieces import PIECES


class Game:
    agent: BaseAgent
    seed: int
    score: int
    running: bool
    board: Board

    def __init__(self, agent: BaseAgent, seed: int = -1) -> None:
        self.agent = agent
        self.seed = seed

        self.score = 0
        self.running = True
        self.board = Board()

    def generate_pieces(self) -> Generator[Piece, None, None]:
        """Generates a list of all the pieces and yields them in order for the game.

        Yields:
            Generator[Piece, None, None]: An instance of the next generated piece in the game.
        """

        random_generator = random.Random(None if self.seed == -1 else self.seed)
        pieces = random_generator.choices(range(7), k=1000)

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
            Board,
            Optional[Action],
        ],
        None,
    ]:
        """Runs the Tetris game. The meat and potatoes of the Tetris tetris.

        Yields: AsyncGenerator[
                    Tuple[Optional[Union[List[Tuple[str, int, int]], List[int]]],
                    int,
                    Board,
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

                # Wait for agent to make a number of moves
                actions = await self.agent.play_move(self.board)
                if isinstance(actions, Action):
                    actions = [actions]

                # Reset the previous board to the current
                old_board = self.board.copy()

                # Perform the action
                for action in actions:
                    self.board.apply_action(action)

                    if self.board.piece.landed:
                        break

                # Yield the changes to the board once the current action has taken place
                # Deals with cases of repeated movement into corner or hard drop when just above another piece
                # Moves are yielded regardless so that they are still recorded
                changes = self.board.get_changes(old_board)
                yield changes, None, self.board, actions

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
