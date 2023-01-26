from typing import List, Tuple, Optional


class TetrisPiece:
    piece_type = "N"

    def __init__(self) -> None:
        self.x = -1
        self.y = -1
        self.orientation = 0
        self.landed = False

    def spawn_piece(self) -> List[Tuple[int, int]]:
        raise NotImplementedError

    def move_left(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        raise NotImplementedError

    def move_right(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        raise NotImplementedError

    def rotate_clockwise(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        raise NotImplementedError

    def rotate_anticlockwise(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        raise NotImplementedError

    def has_landed(self, board: List[List[Optional[str]]]) -> bool:
        raise NotImplementedError

    def fall(self) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
        raise NotImplementedError
