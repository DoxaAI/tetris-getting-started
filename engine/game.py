from typing import Generator, AsyncGenerator, Optional, Tuple

import numpy as np

from engine.actions import Action
from engine.board import TetrisBoard
from engine.piece import TetrisPiece
from engine.pieces import PIECES


class BaseAgent:
    async def play_move(self, board: TetrisBoard) -> Action:
        raise NotImplementedError


class HumanAgent(BaseAgent):
    async def play_move(self, board: TetrisBoard) -> Action:
        move = input()
        if move == "q":
            return Action.ROTATE_ANTICLOCKWISE
        elif move == "e":
            return Action.ROTATE_CLOCKWISE
        elif move == "a":
            return Action.MOVE_LEFT
        elif move == "d":
            return Action.MOVE_RIGHT
        elif move == "s":
            return Action.HARD_DROP

        return Action.NOOP


class LocalTetrisGame:
    def __init__(self, agent: BaseAgent, seed: int = -1) -> None:
        self.seed = seed
        self.score = 0
        self.running = True
        self.agent = agent
        self.board = TetrisBoard()

    def generate_pieces(self) -> Generator[TetrisPiece, None, None]:
        if self.seed != -1:
            np.random.seed(self.seed)

        piece_order = np.random.randint(7, size=1000)  # type: ignore
        piece_counter = 0

        while self.running and piece_counter < 1000:
            piece: TetrisPiece = PIECES[piece_order[piece_counter]]()  # type: ignore
            piece_counter += 1
            self.board.set_piece(piece)
            self.board.spawn_piece()

            yield piece

    async def run(
        self,
    ) -> AsyncGenerator[Tuple[bool, int, TetrisBoard, Optional[Action]], None]:
        for piece in self.generate_pieces():
            yield self.running, self.score, self.board, None

            while not piece.landed:
                move = await self.agent.play_move(self.board)
                assert move.numerator in range(6)

                if move == Action.HARD_DROP:
                    while not piece.landed:
                        self.board.fall()
                else:
                    if move == Action.ROTATE_ANTICLOCKWISE:
                        self.board.rotate_piece_anticlockwise()
                    elif move == Action.ROTATE_CLOCKWISE:
                        self.board.rotate_piece_clockwise()
                    elif move == Action.MOVE_LEFT:
                        self.board.move_piece_left()
                    elif move == Action.MOVE_RIGHT:
                        self.board.move_piece_right()

                    self.board.fall()

                yield self.running, self.score, self.board, move

            self.score += self.board.check_board()
            self.running = self.board.check_endgame()

        yield self.running, self.score, self.board, None


class RemoteTetrisGame:
    pass
