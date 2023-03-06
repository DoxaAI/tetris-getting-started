from typing import List, Optional, Tuple

from tetris.constants import (
    BoardState,
    Cell,
    BOARD_HEIGHT,
    BOARD_WIDTH,
)
from tetris.piece import Piece


class IPiece(Piece):
    piece_type = "I"

    def __init__(self) -> None:
        super().__init__()

        self.x = 4  # I piece x coordinate is the second square from left
        self.y = 1

    def spawn_piece(self) -> List[Cell]:
        return [
            (self.y, self.x - 1),
            (self.y, self.x),
            (self.y, self.x + 1),
            (self.y, self.x + 2),
        ]

    def move_left(
        self, board: BoardState
    ) -> Tuple[Optional[List[Cell]], Optional[List[Cell]]]:
        old, new = None, None

        if self.orientation == 0 and self.x > 1 and not board[self.y][self.x - 2]:
            old = [(self.y, self.x + 2)]
            new = [(self.y, self.x - 2)]

        elif (
            self.orientation == 1
            and self.x > 0
            and not board[self.y - 1][self.x - 1]
            and not board[self.y][self.x - 1]
            and not board[self.y + 1][self.x - 1]
            and not board[self.y + 2][self.x - 1]
        ):
            old = [
                (self.y - 1, self.x),
                (self.y, self.x),
                (self.y + 1, self.x),
                (self.y + 2, self.x),
            ]
            new = [
                (self.y - 1, self.x - 1),
                (self.y, self.x - 1),
                (self.y + 1, self.x - 1),
                (self.y + 2, self.x - 1),
            ]

        elif self.orientation == 2 and self.x > 2 and not board[self.y][self.x - 3]:
            old = [(self.y, self.x + 1)]
            new = [(self.y, self.x - 3)]

        elif (
            self.orientation == 3
            and self.x > 0
            and not board[self.y - 2][self.x - 1]
            and not board[self.y - 1][self.x - 1]
            and not board[self.y][self.x - 1]
            and not board[self.y + 1][self.x - 1]
        ):
            old = [
                (self.y - 2, self.x),
                (self.y - 1, self.x),
                (self.y, self.x),
                (self.y + 1, self.x),
            ]
            new = [
                (self.y - 2, self.x - 1),
                (self.y - 1, self.x - 1),
                (self.y, self.x - 1),
                (self.y + 1, self.x - 1),
            ]

        if old and new:
            self.x -= 1

        return old, new

    def move_right(
        self, board: BoardState
    ) -> Tuple[Optional[List[Cell]], Optional[List[Cell]]]:
        old, new = None, None

        if (
            self.orientation == 0
            and self.x < BOARD_WIDTH - 3
            and not board[self.y][self.x + 3]
        ):
            old = [(self.y, self.x - 1)]
            new = [(self.y, self.x + 3)]

        elif (
            self.orientation == 1
            and self.x < BOARD_WIDTH - 1
            and not board[self.y - 1][self.x + 1]
            and not board[self.y][self.x + 1]
            and not board[self.y + 1][self.x + 1]
            and not board[self.y + 2][self.x + 1]
        ):
            old = [
                (self.y - 1, self.x),
                (self.y, self.x),
                (self.y + 1, self.x),
                (self.y + 2, self.x),
            ]
            new = [
                (self.y - 1, self.x + 1),
                (self.y, self.x + 1),
                (self.y + 1, self.x + 1),
                (self.y + 2, self.x + 1),
            ]

        elif (
            self.orientation == 2
            and self.x < BOARD_WIDTH - 2
            and not board[self.y][self.x + 2]
        ):
            old = [(self.y, self.x - 2)]
            new = [(self.y, self.x + 2)]

        elif (
            self.orientation == 3
            and self.x < BOARD_WIDTH - 1
            and not board[self.y - 2][self.x + 1]
            and not board[self.y - 1][self.x + 1]
            and not board[self.y][self.x + 1]
            and not board[self.y + 1][self.x + 1]
        ):
            old = [
                (self.y - 2, self.x),
                (self.y - 1, self.x),
                (self.y, self.x),
                (self.y + 1, self.x),
            ]
            new = [
                (self.y - 2, self.x + 1),
                (self.y - 1, self.x + 1),
                (self.y, self.x + 1),
                (self.y + 1, self.x + 1),
            ]

        if old and new:
            self.x += 1

        return old, new

    def rotate_clockwise(
        self, board: BoardState
    ) -> Tuple[Optional[List[Cell]], Optional[List[Cell]]]:
        old, new = None, None

        if self.orientation == 0:
            if (
                self.y < BOARD_HEIGHT - 2
                and not board[self.y - 1][self.x + 1]
                and not board[self.y + 1][self.x + 1]
                and not board[self.y + 2][self.x + 1]
            ):
                new = [
                    (self.y - 1, self.x + 1),
                    (self.y + 1, self.x + 1),
                    (self.y + 2, self.x + 1),
                ]
            elif (
                (self.y == BOARD_HEIGHT - 2 or self.y == BOARD_HEIGHT - 1)
                and not board[BOARD_HEIGHT - 1 - ((self.y + 1) % 2)][self.x + 1]
                and not board[BOARD_HEIGHT - 3][self.x + 1]
                and not board[BOARD_HEIGHT - 4][self.x + 1]
            ):
                new = [
                    (BOARD_HEIGHT - 1 - ((self.y + 1) % 2), self.x + 1),
                    (BOARD_HEIGHT - 3, self.x + 1),
                    (BOARD_HEIGHT - 4, self.x + 1),
                ]

        elif self.orientation == 1:
            if (
                self.x == BOARD_WIDTH - 1
                and not board[self.y + 1][self.x - 3]
                and not board[self.y + 1][self.x - 2]
                and not board[self.y + 1][self.x - 1]
            ):
                new = [
                    (self.y + 1, self.x - 3),
                    (self.y + 1, self.x - 2),
                    (self.y + 1, self.x - 1),
                ]

            elif (
                self.x == 0
                and not board[self.y + 1][self.x + 3]
                and not board[self.y + 1][self.x + 2]
                and not board[self.y + 1][self.x + 1]
            ):
                new = [
                    (self.y + 1, self.x + 3),
                    (self.y + 1, self.x + 2),
                    (self.y + 1, self.x + 1),
                ]

            elif (
                self.x == 1
                and not board[self.y + 1][self.x - 1]
                and not board[self.y + 1][self.x + 1]
                and not board[self.y + 1][self.x + 2]
            ):
                new = [
                    (self.y + 1, self.x + 3),
                    (self.y + 1, self.x + 2),
                    (self.y + 1, self.x + 1),
                ]

            elif (
                1 < self.x < BOARD_WIDTH - 1
                and not board[self.y + 1][self.x - 2]
                and not board[self.y + 1][self.x - 1]
                and not board[self.y + 1][self.x + 1]
            ):
                new = [
                    (self.y + 1, self.x - 2),
                    (self.y + 1, self.x - 1),
                    (self.y + 1, self.x + 1),
                ]

        elif self.orientation == 2:
            if (
                self.y < BOARD_HEIGHT - 1
                and not board[self.y - 2][self.x - 1]
                and not board[self.y - 1][self.x - 1]
                and not board[self.y + 1][self.x - 1]
            ):
                new = [
                    (self.y - 2, self.x - 1),
                    (self.y - 1, self.x - 1),
                    (self.y + 1, self.x - 1),
                ]
            elif (
                self.y == BOARD_HEIGHT - 1
                and not board[BOARD_HEIGHT - 4][self.x - 1]
                and not board[BOARD_HEIGHT - 3][self.x - 1]
                and not board[BOARD_HEIGHT - 2][self.x - 1]
            ):
                new = [
                    (BOARD_HEIGHT - 4, self.x - 1),
                    (BOARD_HEIGHT - 3, self.x - 1),
                    (BOARD_HEIGHT - 2, self.x - 1),
                ]

        elif self.orientation == 3:
            if (
                self.x == 0
                and not board[self.y - 1][self.x + 1]
                and not board[self.y - 1][self.x + 2]
                and not board[self.y - 1][self.x + 3]
            ):
                new = [
                    (self.y - 1, self.x + 1),
                    (self.y - 1, self.x + 2),
                    (self.y - 1, self.x + 3),
                ]

            elif (
                self.x == BOARD_WIDTH - 2
                and not board[self.y - 1][self.x - 2]
                and not board[self.y - 1][self.x - 1]
                and not board[self.y - 1][self.x + 1]
            ):
                new = [
                    (self.y - 1, self.x - 2),
                    (self.y - 1, self.x - 1),
                    (self.y - 1, self.x + 1),
                ]

            elif (
                self.x == BOARD_WIDTH - 1
                and not board[self.y - 1][self.x - 3]
                and not board[self.y - 1][self.x - 2]
                and not board[self.y - 1][self.x - 1]
            ):
                new = [
                    (self.y - 1, self.x - 3),
                    (self.y - 1, self.x - 2),
                    (self.y - 1, self.x - 1),
                ]

            elif (
                0 < self.x < BOARD_WIDTH - 2
                and not board[self.y - 1][self.x - 1]
                and not board[self.y - 1][self.x + 1]
                and not board[self.y - 1][self.x + 2]
            ):
                new = [
                    (self.y - 1, self.x - 1),
                    (self.y - 1, self.x + 1),
                    (self.y - 1, self.x + 2),
                ]

        else:
            raise ValueError("Incorrect value for orientation")

        if new:
            if self.orientation == 0:
                old = [(self.y, self.x - 1), (self.y, self.x), (self.y, self.x + 2)]
                self.x += 1
                if self.y == BOARD_HEIGHT - 2 or self.y == BOARD_HEIGHT - 1:
                    self.y = BOARD_HEIGHT - 3
            elif self.orientation == 1:
                old = [(self.y - 1, self.x), (self.y, self.x), (self.y + 2, self.x)]
                self.y += 1
                if self.x == BOARD_WIDTH - 1:
                    self.x -= 1
                elif self.x == 0 or self.x == 1:
                    self.x = 2
            elif self.orientation == 2:
                old = [(self.y, self.x - 2), (self.y, self.x), (self.y, self.x + 1)]
                self.x -= 1
                if self.y == BOARD_HEIGHT - 1:
                    self.y = BOARD_HEIGHT - 2
            elif self.orientation == 3:
                old = [(self.y + 1, self.x), (self.y, self.x), (self.y - 2, self.x)]
                self.y -= 1
                if self.x == 0:
                    self.x += 1
                elif self.x == BOARD_WIDTH - 2 or self.x == BOARD_WIDTH - 1:
                    self.x = BOARD_WIDTH - 3
            else:
                raise ValueError("Incorrect value for orientation")

            self.orientation = (self.orientation + 1) % 4

        return old, new

    def rotate_anticlockwise(
        self, board: BoardState
    ) -> Tuple[Optional[List[Cell]], Optional[List[Cell]]]:
        old, new = None, None

        if self.orientation == 0:
            if (
                self.y < BOARD_HEIGHT - 2
                and not board[self.y - 1][self.x]
                and not board[self.y + 1][self.x]
                and not board[self.y + 2][self.x]
            ):
                new = [
                    (self.y - 1, self.x),
                    (self.y + 1, self.x),
                    (self.y + 2, self.x),
                ]

            elif (
                (self.y == BOARD_HEIGHT - 2 or self.y == BOARD_HEIGHT - 1)
                and not board[BOARD_HEIGHT - 4][self.x]
                and not board[BOARD_HEIGHT - 3][self.x]
                and not board[BOARD_HEIGHT - 1 - ((self.y + 1) % 2)][self.x]
            ):
                new = [
                    (BOARD_HEIGHT - 4, self.x),
                    (BOARD_HEIGHT - 3, self.x),
                    (BOARD_HEIGHT - 1 - ((self.y + 1) % 2), self.x),
                ]

        elif self.orientation == 1:
            if (
                self.x == BOARD_WIDTH - 1
                and not board[self.y][self.x - 3]
                and not board[self.y][self.x - 2]
                and not board[self.y][self.x - 1]
            ):
                new = [
                    (self.y, self.x - 3),
                    (self.y, self.x - 2),
                    (self.y, self.x - 1),
                ]

            elif (
                self.x == 0
                and not board[self.y][self.x + 1]
                and not board[self.y][self.x + 2]
                and not board[self.y][self.x + 3]
            ):
                new = [
                    (self.y, self.x + 1),
                    (self.y, self.x + 2),
                    (self.y, self.x + 3),
                ]

            elif (
                self.x == 1
                and not board[self.y][self.x - 1]
                and not board[self.y][self.x + 1]
                and not board[self.y][self.x + 2]
            ):
                new = [
                    (self.y, self.x - 1),
                    (self.y, self.x + 1),
                    (self.y, self.x + 2),
                ]

            elif (
                1 < self.x < BOARD_WIDTH - 1
                and not board[self.y][self.x - 2]
                and not board[self.y][self.x - 1]
                and not board[self.y][self.x + 1]
            ):
                new = [
                    (self.y, self.x - 2),
                    (self.y, self.x - 1),
                    (self.y, self.x + 1),
                ]

        elif self.orientation == 2:
            if (
                self.y < BOARD_HEIGHT - 1
                and not board[self.y - 2][self.x]
                and not board[self.y - 1][self.x]
                and not board[self.y + 1][self.x]
            ):
                new = [
                    (self.y - 2, self.x),
                    (self.y - 1, self.x),
                    (self.y + 1, self.x),
                ]

            elif (
                self.y == BOARD_HEIGHT - 1
                and not board[BOARD_HEIGHT - 4][self.x]
                and not board[BOARD_HEIGHT - 3][self.x]
                and not board[BOARD_HEIGHT - 2][self.x]
            ):
                new = [
                    (BOARD_HEIGHT - 4, self.x),
                    (BOARD_HEIGHT - 3, self.x),
                    (BOARD_HEIGHT - 2, self.x),
                ]

        elif self.orientation == 3:
            if (
                self.x == 0
                and not board[self.y][self.x + 1]
                and not board[self.y][self.x + 2]
                and not board[self.y][self.x + 3]
            ):
                new = [
                    (self.y, self.x + 1),
                    (self.y, self.x + 2),
                    (self.y, self.x + 3),
                ]

            elif (
                self.x == BOARD_WIDTH - 2
                and not board[self.y][self.x - 2]
                and not board[self.y][self.x - 1]
                and not board[self.y][self.x + 1]
            ):
                new = [
                    (self.y, self.x - 2),
                    (self.y, self.x - 1),
                    (self.y, self.x + 1),
                ]

            elif (
                self.x == BOARD_WIDTH - 1
                and not board[self.y][self.x - 3]
                and not board[self.y][self.x - 2]
                and not board[self.y][self.x - 1]
            ):
                new = [
                    (self.y, self.x - 3),
                    (self.y, self.x - 2),
                    (self.y, self.x - 1),
                ]

            elif (
                0 < self.x < BOARD_WIDTH - 2
                and not board[self.y][self.x - 1]
                and not board[self.y][self.x + 1]
                and not board[self.y][self.x + 2]
            ):
                new = [
                    (self.y, self.x - 1),
                    (self.y, self.x + 1),
                    (self.y, self.x + 2),
                ]

        else:
            raise ValueError("Incorrect value for orientation")

        if new:
            if self.orientation == 0:
                old = [(self.y, self.x - 1), (self.y, self.x + 1), (self.y, self.x + 2)]
                if self.y == BOARD_HEIGHT - 2 or self.y == BOARD_HEIGHT - 1:
                    self.y = BOARD_HEIGHT - 2
                else:
                    self.y += 1
            elif self.orientation == 1:
                old = [(self.y - 1, self.x), (self.y + 1, self.x), (self.y + 2, self.x)]
                if self.x == BOARD_WIDTH - 1:
                    self.x -= 2
                elif self.x == 0 or self.x == 1:
                    self.x = 1
                else:
                    self.x -= 1
            elif self.orientation == 2:
                old = [(self.y, self.x - 2), (self.y, self.x - 1), (self.y, self.x + 1)]
                if self.y == BOARD_HEIGHT - 1:
                    self.y = BOARD_HEIGHT - 3
                else:
                    self.y -= 1
            elif self.orientation == 3:
                old = [(self.y - 2, self.x), (self.y - 1, self.x), (self.y + 1, self.x)]
                if self.x == 0:
                    self.x += 2
                elif self.x == BOARD_WIDTH - 2 or self.x == BOARD_WIDTH - 1:
                    self.x = BOARD_WIDTH - 2
                else:
                    self.x += 1
            else:
                raise ValueError("Incorrect value for orientation")

            self.orientation = (self.orientation - 1) % 4

        return old, new

    def has_landed(self, board: BoardState) -> bool:
        if self.orientation == 0 and (
            self.y == BOARD_HEIGHT - 1
            or board[self.y + 1][self.x - 1]
            or board[self.y + 1][self.x]
            or board[self.y + 1][self.x + 1]
            or board[self.y + 1][self.x + 2]
        ):
            return True

        elif self.orientation == 1 and (
            self.y == BOARD_HEIGHT - 3 or board[self.y + 3][self.x]
        ):
            return True

        elif self.orientation == 2 and (
            self.y == BOARD_HEIGHT - 1
            or board[self.y + 1][self.x - 2]
            or board[self.y + 1][self.x - 1]
            or board[self.y + 1][self.x]
            or board[self.y + 1][self.x + 1]
        ):
            return True

        elif self.orientation == 3 and (
            self.y == BOARD_HEIGHT - 2 or board[self.y + 2][self.x]
        ):
            return True

        return False

    def fall(self) -> Tuple[List[Cell], List[Cell]]:
        self.y += 1

        if self.orientation == 0:
            old = [
                (self.y - 1, self.x - 1),
                (self.y - 1, self.x),
                (self.y - 1, self.x + 1),
                (self.y - 1, self.x + 2),
            ]
            new = [
                (self.y, self.x - 1),
                (self.y, self.x),
                (self.y, self.x + 1),
                (self.y, self.x + 2),
            ]

        elif self.orientation == 1:
            old = [(self.y - 2, self.x)]
            new = [(self.y + 2, self.x)]

        elif self.orientation == 2:
            old = [
                (self.y - 1, self.x - 2),
                (self.y - 1, self.x - 1),
                (self.y - 1, self.x),
                (self.y - 1, self.x + 1),
            ]
            new = [
                (self.y, self.x - 2),
                (self.y, self.x - 1),
                (self.y, self.x),
                (self.y, self.x + 1),
            ]

        elif self.orientation == 3:
            old = [(self.y - 3, self.x)]
            new = [(self.y + 1, self.x)]

        else:
            raise ValueError("Incorrect value for orientation")

        return old, new
