from typing import List, Tuple, Optional

from engine.piece import TetrisPiece


class OPiece(TetrisPiece):
    piece_type = "O"

    def __init__(self) -> None:
        super().__init__()

        self.x = 4  # O piece x coordinate is the bottom left square
        self.y = 2

    def spawn_piece(self) -> List[Tuple[int, int]]:
        new = [
            (self.y, self.x),
            (self.y - 1, self.x),
            (self.y - 1, self.x + 1),
            (self.y, self.x + 1),
        ]

        return new

    def move_left(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        old, new = None, None

        if (
            self.x > 0
            and not board[self.y][self.x - 1]
            and not board[self.y - 1][self.x - 1]
        ):
            self.x -= 1
            old = [(self.y, self.x + 2), (self.y - 1, self.x + 2)]
            new = [(self.y, self.x), (self.y - 1, self.x)]

        return old, new

    def move_right(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        old, new = None, None

        if (
            self.x < 8
            and not board[self.y][self.x + 2]
            and not board[self.y - 1][self.x + 2]
        ):
            self.x += 1
            old = [(self.y, self.x - 1), (self.y - 1, self.x - 1)]
            new = [(self.y, self.x + 1), (self.y - 1, self.x + 1)]

        return old, new

    def rotate_clockwise(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        self.orientation = 0
        return None, None

    def rotate_anticlockwise(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        self.orientation = 0
        return None, None

    def has_landed(self, board: List[List[Optional[str]]]) -> bool:
        if self.y == 20 or board[self.y + 1][self.x] or board[self.y + 1][self.x + 1]:
            return True

        return False

    def fall(self) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
        self.y += 1
        old = [(self.y - 2, self.x), (self.y - 2, self.x + 1)]
        new = [(self.y, self.x), (self.y, self.x + 1)]

        return old, new
