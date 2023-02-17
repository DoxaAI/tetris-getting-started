import copy
from typing import Dict, List, Optional, Tuple

from engine.actions import Action
from engine.piece import TetrisPiece

LINE_CLEAR_SCORES: Dict[int, int] = {1: 100, 2: 250, 3: 750, 4: 3000}

BOARD_WIDTH = 10
BOARD_HEIGHT = 21


class TetrisBoard:
    board: List[List[Optional[str]]]
    piece: Optional[TetrisPiece]
    running: bool

    def __init__(self) -> None:
        self.board = [[None] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.piece = None

    def set_piece(self, piece: TetrisPiece) -> None:
        """Sets a piece to be the current piece being controlled.

        Args:
            piece (TetrisPiece): Any one of the Tetris pieces.
        """
        self.piece = piece

    def is_game_running(self) -> bool:
        """Checks the board to see if there are any cells filled in the top playable row.
           If there are, the player has lost the game.

        Returns:
            bool: False if the board has any pieces in the top row else True.
        """

        return self.board[1].count(None) == BOARD_WIDTH

    def copy(self) -> List[List[Optional[str]]]:
        """Copies the internal board state.

        Returns:
            List[List[Optional[str]]]: The board.
        """

        return copy.deepcopy(self.board)

    def get_changes(
        self, old_board: List[List[Optional[str]]]
    ) -> List[Tuple[str, int, int]]:
        """Identifies differences between the current board and another board state.

        Args:
            old_board (List[List[Optional[str]]]): The board to compare against.

        Returns:
            List[Tuple[str, int, int]]: A list of changes in the form (cell_value, y, x).
        """

        return [
            ("N" if not self.board[i][j] else self.board[i][j], i, j)
            for i, row in enumerate(old_board)
            for j, x in enumerate(row)
            if self.board[i][j] != x
        ]

    def find_lines_to_clear(self) -> List[int]:
        """Iterates through each row in the board to see if it's full and can be cleared.

        Returns:
            List[int]: Indices of each row that needs to be cleared.
        """

        return [i for i in reversed(range(BOARD_HEIGHT)) if None not in self.board[i]]

    def clear_lines(self, line_indices: List[int]) -> int:
        """Removes each row to be cleared from the board and adds empty rows to the top.
           Gets the score based on how many rows have been cleared.

        Args:
            line_indices (List[int]): The list of index rows to be cleared.

        Returns:
            int: The score that the number of cleared lines are worth.
        """

        if not line_indices:
            return 0

        for i in line_indices:
            del self.board[i]

        self.board = [
            [None] * BOARD_WIDTH for _ in range(len(line_indices))
        ] + self.board

        return LINE_CLEAR_SCORES[len(line_indices)]

    def update_board(
        self, old: List[Tuple[int, int]], new: List[Tuple[int, int]]
    ) -> None:
        """Updates the board based on old and new locations of the current piece.

        Args:
            old (List[Tuple[int, int]]): The old (y, x) coordinates of the piece to be removed.
            new (List[Tuple[int, int]]): The new (y, x) coordinates of the piece to be added.
        """

        # old or new can be empty lists if nothing needs to be removed or added

        for old_cell in old:
            self.board[old_cell[0]][old_cell[1]] = None

        for new_cell in new:
            self.board[new_cell[0]][new_cell[1]] = self.piece.piece_type

    def spawn_piece(self) -> bool:
        """Spawns the board object's current piece on the board.

        If this piece has spawned inside another piece, set it to landed.

        Returns:
            bool: Whether the piece could be spawned successfully
        """

        new_piece_location = self.piece.spawn_piece()
        for coord in new_piece_location:
            if self.board[coord[0]][coord[1]]:
                self.piece.landed = True
                return False

        self.update_board([], new_piece_location)

        return True

    def move_piece_left(self) -> None:
        """Calls the current piece's function to move left and updates board if required."""

        old, new = self.piece.move_left(self.board)

        if old and new:
            self.update_board(old, new)

    def move_piece_right(self) -> None:
        """Calls the current piece's function to move right and updates board if required."""

        old, new = self.piece.move_right(self.board)

        if old and new:
            self.update_board(old, new)

    def rotate_piece_clockwise(self) -> None:
        """Calls the current piece's function to rotate clockwise and updates board if required."""

        old, new = self.piece.rotate_clockwise(self.board)

        if old and new:
            self.update_board(old, new)

    def rotate_piece_anticlockwise(self) -> None:
        """Calls the current piece's function to rotate anticlockwise and updates board if required."""

        old, new = self.piece.rotate_anticlockwise(self.board)

        if old and new:
            self.update_board(old, new)

    def fall(self) -> None:
        """Calls the current piece's function to fall one step if it hasn't landed and updates board if required."""

        self.piece.landed = self.piece.has_landed(self.board)
        if not self.piece.landed:
            old, new = self.piece.fall()
            self.update_board(old, new)

    def apply_action(self, action: Action) -> None:
        """Applies an action to the current board.

        Args:
            move (Action): The action to apply.
        """

        if action == Action.HARD_DROP:
            while not self.piece.landed:
                self.fall()
            return
        elif action == Action.ROTATE_ANTICLOCKWISE:
            self.rotate_piece_anticlockwise()
        elif action == Action.ROTATE_CLOCKWISE:
            self.rotate_piece_clockwise()
        elif action == Action.MOVE_LEFT:
            self.move_piece_left()
        elif action == Action.MOVE_RIGHT:
            self.move_piece_right()

        self.fall()

    def with_move(self, action: Action) -> "TetrisBoard":
        """Creates a copy of the current board object and applies an action to that board.
           Used to see how the board would look at the next time step if an action has been taken.

        Args:
            action (Action): The action to be applied to the copy of the board.

        Returns:
            TetrisBoard: A copy of the current board with the action applied to it with the fall step after.
        """

        board = copy.deepcopy(self)

        board.apply_action(action)

        return board
