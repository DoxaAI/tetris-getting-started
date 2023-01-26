from typing import List, Tuple, Optional

from engine.piece import TetrisPiece


class JPiece(TetrisPiece):
    piece_type = "J"

    def __init__(self) -> None:
        super().__init__()

        self.x = 4  # J piece x coordinate is the bottom one in the middle, starts like |_ _ _
        self.y = 2

    def spawn_piece(self) -> List[Tuple[int, int]]:
        new = [
            (self.y - 1, self.x - 1),
            (self.y, self.x - 1),
            (self.y, self.x),
            (self.y, self.x + 1),
        ]

        return new

    def move_left(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        old, new = None, None

        if self.orientation == 0:
            if (
                self.x > 1
                and not board[self.y - 1][self.x - 2]
                and not board[self.y][self.x - 2]
            ):
                old = [(self.y - 1, self.x - 1), (self.y, self.x + 1)]
                new = [(self.y - 1, self.x - 2), (self.y, self.x - 2)]

        elif self.orientation == 1:
            if (
                self.x > 0
                and not board[self.y - 1][self.x - 1]
                and not board[self.y][self.x - 1]
                and not board[self.y + 1][self.x - 1]
            ):
                old = [(self.y - 1, self.x + 1), (self.y, self.x), (self.y + 1, self.x)]
                new = [
                    (self.y - 1, self.x - 1),
                    (self.y, self.x - 1),
                    (self.y + 1, self.x - 1),
                ]

        elif self.orientation == 2:
            if (
                self.x > 1
                and not board[self.y][self.x - 2]
                and not board[self.y + 1][self.x]
            ):
                old = [(self.y, self.x + 1), (self.y + 1, self.x + 1)]
                new = [(self.y, self.x - 2), (self.y + 1, self.x)]

        elif self.orientation == 3:
            if (
                self.x > 1
                and not board[self.y - 1][self.x - 1]
                and not board[self.y][self.x - 1]
                and not board[self.y + 1][self.x - 2]
            ):
                old = [(self.y - 1, self.x), (self.y, self.x), (self.y + 1, self.x)]
                new = [
                    (self.y - 1, self.x - 1),
                    (self.y, self.x - 1),
                    (self.y + 1, self.x - 2),
                ]

        if old and new:
            self.x -= 1

        return old, new

    def move_right(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        old, new = None, None

        if self.orientation == 0:
            if (
                self.x < 8
                and not board[self.y - 1][self.x]
                and not board[self.y][self.x + 2]
            ):
                old = [(self.y - 1, self.x - 1), (self.y, self.x - 1)]
                new = [(self.y - 1, self.x), (self.y, self.x + 2)]

        elif self.orientation == 1:
            if (
                self.x < 8
                and not board[self.y - 1][self.x + 2]
                and not board[self.y][self.x + 1]
                and not board[self.y + 1][self.x + 1]
            ):
                old = [(self.y - 1, self.x), (self.y, self.x), (self.y + 1, self.x)]
                new = [
                    (self.y - 1, self.x + 2),
                    (self.y, self.x + 1),
                    (self.y + 1, self.x + 1),
                ]

        elif self.orientation == 2:
            if (
                self.x < 8
                and not board[self.y][self.x + 2]
                and not board[self.y + 1][self.x + 2]
            ):
                old = [(self.y, self.x - 1), (self.y + 1, self.x + 1)]
                new = [(self.y, self.x + 1), (self.y + 1, self.x + 2)]

        elif self.orientation == 3:
            if (
                self.x < 9
                and not board[self.y - 1][self.x + 1]
                and not board[self.y][self.x + 1]
                and not board[self.y + 1][self.x + 1]
            ):
                old = [(self.y - 1, self.x), (self.y, self.x), (self.y + 1, self.x - 1)]
                new = [
                    (self.y - 1, self.x + 1),
                    (self.y, self.x + 1),
                    (self.y + 1, self.x + 1),
                ]

        if old and new:
            self.x += 1

        return old, new

    def rotate_clockwise(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        old, new = None, None

        if self.orientation == 0:
            if (
                self.y < 20
                and not board[self.y + 1][self.x]
                and not board[self.y - 1][self.x]
                and not board[self.y - 1][self.x + 1]
            ):
                new = [
                    (self.y + 1, self.x),
                    (self.y - 1, self.x),
                    (self.y - 1, self.x + 1),
                ]

        elif self.orientation == 1:
            if self.x == 0:
                if (
                    not board[self.y][self.x + 1]
                    and not board[self.y][self.x + 2]
                    and not board[self.y + 1][self.x + 2]
                ):
                    new = [
                        (self.y, self.x + 1),
                        (self.y, self.x + 2),
                        (self.y + 1, self.x + 2),
                    ]

            else:
                if (
                    not board[self.y][self.x - 1]
                    and not board[self.y][self.x + 1]
                    and not board[self.y + 1][self.x + 1]
                ):
                    new = [
                        (self.y, self.x - 1),
                        (self.y, self.x + 1),
                        (self.y + 1, self.x + 1),
                    ]

        elif self.orientation == 2:
            if (
                not board[self.y - 1][self.x]
                and not board[self.y + 1][self.x]
                and not board[self.y + 1][self.x - 1]
            ):
                new = [
                    (self.y - 1, self.x),
                    (self.y + 1, self.x),
                    (self.y + 1, self.x - 1),
                ]

        elif self.orientation == 3:
            if self.x == 9:
                if (
                    not board[self.y][self.x - 1]
                    and not board[self.y][self.x - 2]
                    and not board[self.y - 1][self.x - 2]
                ):
                    new = [
                        (self.y, self.x - 1),
                        (self.y, self.x - 2),
                        (self.y - 1, self.x - 2),
                    ]

            else:
                if (
                    not board[self.y][self.x + 1]
                    and not board[self.y][self.x - 1]
                    and not board[self.y - 1][self.x - 1]
                ):
                    new = [
                        (self.y, self.x + 1),
                        (self.y, self.x - 1),
                        (self.y - 1, self.x - 1),
                    ]

        else:
            raise ValueError("Incorrect value for orientation")

        if new:
            if self.orientation == 0:
                old = [
                    (self.y - 1, self.x - 1),
                    (self.y, self.x - 1),
                    (self.y, self.x + 1),
                ]
            elif self.orientation == 1:
                old = [
                    (self.y + 1, self.x),
                    (self.y - 1, self.x),
                    (self.y - 1, self.x + 1),
                ]
                if self.x == 0:
                    self.x += 1
            elif self.orientation == 2:
                old = [
                    (self.y, self.x - 1),
                    (self.y, self.x + 1),
                    (self.y + 1, self.x + 1),
                ]
            elif self.orientation == 3:
                old = [
                    (self.y - 1, self.x),
                    (self.y + 1, self.x),
                    (self.y + 1, self.x - 1),
                ]
                if self.x == 9:
                    self.x -= 1
            else:
                raise ValueError("Incorrect value for orientation")

            self.orientation = (self.orientation + 1) % 4

        return old, new

    def rotate_anticlockwise(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        old, new = None, None

        if self.orientation == 0:
            if (
                self.y < 20
                and not board[self.y - 1][self.x]
                and not board[self.y + 1][self.x]
                and not board[self.y + 1][self.x - 1]
            ):
                new = [
                    (self.y - 1, self.x),
                    (self.y + 1, self.x),
                    (self.y + 1, self.x - 1),
                ]

        elif self.orientation == 1:
            if self.x == 0:
                if not board[self.y][self.x + 1] and not board[self.y][self.x + 2]:
                    new = [(self.y, self.x + 1), (self.y, self.x + 2)]

            else:
                if (
                    not board[self.y - 1][self.x - 1]
                    and not board[self.y][self.x - 1]
                    and not board[self.y][self.x + 1]
                ):
                    new = [
                        (self.y - 1, self.x - 1),
                        (self.y, self.x - 1),
                        (self.y, self.x + 1),
                    ]

        elif self.orientation == 2:
            if (
                not board[self.y - 1][self.x + 1]
                and not board[self.y - 1][self.x]
                and not board[self.y + 1][self.x]
            ):
                new = [
                    (self.y - 1, self.x + 1),
                    (self.y - 1, self.x),
                    (self.y + 1, self.x),
                ]

        elif self.orientation == 3:
            if self.x == 9:
                if not board[self.y][self.x - 1] and not board[self.y][self.x - 2]:
                    new = [(self.y, self.x - 1), (self.y, self.x - 2)]

            else:
                if (
                    not board[self.y][self.x - 1]
                    and not board[self.y][self.x + 1]
                    and not board[self.y + 1][self.x + 1]
                ):
                    new = [
                        (self.y, self.x - 1),
                        (self.y, self.x + 1),
                        (self.y + 1, self.x + 1),
                    ]

        else:
            raise ValueError("Incorrect value for orientation")

        if new:
            if self.orientation == 0:
                old = [
                    (self.y - 1, self.x - 1),
                    (self.y, self.x - 1),
                    (self.y, self.x + 1),
                ]
            elif self.orientation == 1:
                if self.x == 0:
                    old = [(self.y - 1, self.x + 1), (self.y + 1, self.x)]
                    self.x += 1
                else:
                    old = [
                        (self.y + 1, self.x),
                        (self.y - 1, self.x),
                        (self.y - 1, self.x + 1),
                    ]
            elif self.orientation == 2:
                old = [
                    (self.y, self.x - 1),
                    (self.y, self.x + 1),
                    (self.y + 1, self.x + 1),
                ]
            elif self.orientation == 3:
                if self.x == 9:
                    old = [(self.y - 1, self.x), (self.y + 1, self.x - 1)]
                    self.x -= 1
                else:
                    old = [
                        (self.y - 1, self.x),
                        (self.y + 1, self.x),
                        (self.y + 1, self.x - 1),
                    ]
            else:
                raise ValueError("Incorrect value for orientation")

            self.orientation = (self.orientation - 1) % 4

        return old, new

    def has_landed(self, board: List[List[Optional[str]]]) -> bool:
        if self.orientation == 0:
            if (
                self.y == 20
                or board[self.y + 1][self.x - 1]
                or board[self.y + 1][self.x]
                or board[self.y + 1][self.x + 1]
            ):
                return True

        elif self.orientation == 1:
            if self.y == 19 or board[self.y][self.x + 1] or board[self.y + 2][self.x]:
                return True

        elif self.orientation == 2:
            if (
                self.y == 19
                or board[self.y + 1][self.x - 1]
                or board[self.y + 1][self.x]
                or board[self.y + 2][self.x + 1]
            ):
                return True

        elif self.orientation == 3:
            if (
                self.y == 19
                or board[self.y + 2][self.x - 1]
                or board[self.y + 2][self.x]
            ):
                return True

        return False

    def fall(self) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
        self.y += 1

        if self.orientation == 0:
            old = [
                (self.y - 2, self.x - 1),
                (self.y - 1, self.x),
                (self.y - 1, self.x + 1),
            ]
            new = [(self.y, self.x - 1), (self.y, self.x), (self.y, self.x + 1)]

        elif self.orientation == 1:
            old = [(self.y - 2, self.x), (self.y - 2, self.x + 1)]
            new = [(self.y - 1, self.x + 1), (self.y + 1, self.x)]

        elif self.orientation == 2:
            old = [
                (self.y - 1, self.x - 1),
                (self.y - 1, self.x),
                (self.y - 1, self.x + 1),
            ]
            new = [(self.y, self.x - 1), (self.y, self.x), (self.y + 1, self.x + 1)]

        elif self.orientation == 3:
            old = [(self.y - 2, self.x), (self.y, self.x - 1)]
            new = [(self.y + 1, self.x - 1), (self.y + 1, self.x)]

        else:
            raise ValueError("Incorrect value for orientation")

        return old, new
