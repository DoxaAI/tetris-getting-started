from typing import List, Dict, Tuple, Optional
import copy

from engine.piece import TetrisPiece
from engine.actions import Action


class TetrisBoard:
    def __init__(self) -> None:
        self.board: List[List[Optional[str]]] = [[None] * 10 for _ in range(21)]
        self.score_dict: Dict[int, int] = {1: 100, 2: 250, 3: 750, 4: 3000}
        self.piece: TetrisPiece = TetrisPiece()

    def set_piece(self, piece: TetrisPiece) -> None:
        self.piece = piece

    def check_endgame(self) -> bool:
        return self.board[1].count(None) == len(self.board[0])

    def check_board(self) -> int:
        lines_cleared: List[int] = []

        for i in range(len(self.board)):
            if None not in self.board[i]:
                lines_cleared.append(i)

        if len(lines_cleared) > 0:
            lines_cleared.reverse()

            for i in lines_cleared:
                del self.board[i]

            top: List[List[Optional[str]]] = [
                [None] * 10 for _ in range(len(lines_cleared))
            ]

            self.board = top + self.board

            return self.score_dict[len(lines_cleared)]

        return 0

    def update_board(
        self, old: List[Tuple[int, int]], new: List[Tuple[int, int]]
    ) -> None:
        for old_place in old:
            self.board[old_place[0]][old_place[1]] = None

        for new_place in new:
            self.board[new_place[0]][new_place[1]] = self.piece.piece_type

    def spawn_piece(self) -> None:
        self.update_board([], self.piece.spawn_piece())

    def move_piece_left(self) -> None:
        old, new = self.piece.move_left(self.board)

        if old and new:
            self.update_board(old, new)

    def move_piece_right(self) -> None:
        old, new = self.piece.move_right(self.board)

        if old and new:
            self.update_board(old, new)

    def rotate_piece_clockwise(self) -> None:
        old, new = self.piece.rotate_clockwise(self.board)

        if old and new:
            self.update_board(old, new)

    def rotate_piece_anticlockwise(self) -> None:
        old, new = self.piece.rotate_anticlockwise(self.board)

        if old and new:
            self.update_board(old, new)

    def fall(self) -> None:
        self.piece.landed = self.piece.has_landed(self.board)
        if not self.piece.landed:
            old, new = self.piece.fall()
            self.update_board(old, new)

    def with_move(self, action: Action) -> "TetrisBoard":
        temp_board = copy.deepcopy(self)

        if action == Action.HARD_DROP:
            while not temp_board.piece.landed:
                temp_board.fall()
        else:
            if action == Action.ROTATE_ANTICLOCKWISE:
                temp_board.rotate_piece_anticlockwise()
            elif action == Action.ROTATE_CLOCKWISE:
                temp_board.rotate_piece_clockwise()
            elif action == Action.MOVE_LEFT:
                temp_board.move_piece_left()
            elif action == Action.MOVE_RIGHT:
                temp_board.move_piece_right()

            temp_board.fall()

        return temp_board
