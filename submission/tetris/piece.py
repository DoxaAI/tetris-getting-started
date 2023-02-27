from typing import List, Optional, Tuple

from tetris.constants import BoardState, Cell


class Piece:
    piece_type = "N"

    def __init__(self) -> None:
        self.x = -1
        self.y = -1
        self.orientation = 0
        self.landed = False

    def spawn_piece(self) -> List[Cell]:
        """Gets the cells of where this piece will spawn.

        Returns:
            List[Cell]: List of cells where this piece will spawn in the form (y, x)
        """

        raise NotImplementedError

    def move_left(
        self, board: BoardState
    ) -> Tuple[Optional[List[Cell]], Optional[List[Cell]]]:
        """Gets the changed coordinates of the piece when it is moved left on the current board state.

        Args:
            board (BoardState): The current 2D list of the board state.

        Returns:
            Tuple[Optional[List[Cell]], Optional[List[Cell]]]:
            Lists of old and new piece locations after the move in the form ([(old_y1, old_x1), ...], [(new_y1, new_x1), ...]).
        """

        raise NotImplementedError

    def move_right(
        self, board: BoardState
    ) -> Tuple[Optional[List[Cell]], Optional[List[Cell]]]:
        """Gets the changed coordinates of the piece when it is moved right on the current board state.

        Args:
            board (BoardState): The current 2D list of the board state.

        Returns:
            Tuple[Optional[List[Cell]], Optional[List[Cell]]]:
            Lists of old and new piece locations after the move in the form ([(old_y1, old_x1), ...], [(new_y1, new_x1), ...]).
        """

        raise NotImplementedError

    def rotate_clockwise(
        self, board: BoardState
    ) -> Tuple[Optional[List[Cell]], Optional[List[Cell]]]:
        """Gets the changed coordinates of the piece when it is rotated clockwise on the current board state.

        Args:
            board (BoardState): The current 2D list of the board state.

        Returns:
            Tuple[Optional[List[Cell]], Optional[List[Cell]]]:
            Lists of old and new piece locations after the rotation in the form ([(old_y1, old_x1), ...], [(new_y1, new_x1), ...]).
        """

        raise NotImplementedError

    def rotate_anticlockwise(
        self, board: BoardState
    ) -> Tuple[Optional[List[Cell]], Optional[List[Cell]]]:
        """Gets the changed coordinates of the piece when it is rotated anticlockwise on the current board state.

        Args:
            board (BoardState): The current 2D list of the board state.

        Returns:
            Tuple[Optional[List[Cell]], Optional[List[Cell]]]:
            Lists of old and new piece locations after the rotation in the form ([(old_y1, old_x1), ...], [(new_y1, new_x1), ...]).
        """

        raise NotImplementedError

    def has_landed(self, board: BoardState) -> bool:
        """Checks whether the piece has landed on the current board state.

        Args:
            board (BoardState): The current 2D list of the board state.

        Returns:
            bool: True if the piece has landed else False.
        """

        raise NotImplementedError

    def fall(self) -> Tuple[List[Cell], List[Cell]]:
        """Gets the changed coordinates of the piece when it falls.

        Returns:
            Tuple[Optional[List[Cell]], Optional[List[Cell]]]:
            Lists of old and new piece locations after the fall in the form ([(old_y1, old_x1), ...], [(new_y1, new_x1), ...]).
        """

        raise NotImplementedError
