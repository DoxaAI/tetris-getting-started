from __future__ import annotations
from typing import List, Dict, Tuple, Optional
from enum import IntEnum
import copy

###############################################################
#   You most likely will not need to edit this file at all,   #
#   but you should include it as part of your submission.     #
###############################################################


class Action(IntEnum):
    NOOP = 0
    ROTATE_ANTICLOCKWISE = 1
    ROTATE_CLOCKWISE = 2
    MOVE_LEFT = 3
    MOVE_RIGHT = 4
    HARD_DROP = 5


class TetrisPiece:
    piece_type = "N"

    def __init__(self) -> None:
        self.x = -1
        self.y = -1
        self.orientation = 0
        self.landed = False

    def spawn_piece(self) -> List[Tuple[int, int]]:
        """Gets the cells of where this piece will spawn.

        Returns:
            List[Tuple[int, int]]: List of cells where this piece will spawn in the form (y, x)
        """

        raise NotImplementedError

    def move_left(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        """Gets the changed coordinates of the piece when it is moved left on the current board state.

        Args:
            board (List[List[Optional[str]]]): The current 2D list of the board state.

        Returns:
            Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
            Lists of old and new piece locations after the move in the form ([(old_y1, old_x1), ...], [(new_y1, new_x1), ...]).
        """

        raise NotImplementedError

    def move_right(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        """Gets the changed coordinates of the piece when it is moved right on the current board state.

        Args:
            board (List[List[Optional[str]]]): The current 2D list of the board state.

        Returns:
            Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
            Lists of old and new piece locations after the move in the form ([(old_y1, old_x1), ...], [(new_y1, new_x1), ...]).
        """

        raise NotImplementedError

    def rotate_clockwise(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        """Gets the changed coordinates of the piece when it is rotated clockwise on the current board state.

        Args:
            board (List[List[Optional[str]]]): The current 2D list of the board state.

        Returns:
            Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
            Lists of old and new piece locations after the rotation in the form ([(old_y1, old_x1), ...], [(new_y1, new_x1), ...]).
        """

        raise NotImplementedError

    def rotate_anticlockwise(
        self, board: List[List[Optional[str]]]
    ) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        """Gets the changed coordinates of the piece when it is rotated anticlockwise on the current board state.

        Args:
            board (List[List[Optional[str]]]): The current 2D list of the board state.

        Returns:
            Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
            Lists of old and new piece locations after the rotation in the form ([(old_y1, old_x1), ...], [(new_y1, new_x1), ...]).
        """

        raise NotImplementedError

    def has_landed(self, board: List[List[Optional[str]]]) -> bool:
        """Checks whether the piece has landed on the current board state.

        Args:
            board (List[List[Optional[str]]]): The current 2D list of the board state.

        Returns:
            bool: True if the piece has landed else False.
        """

        raise NotImplementedError

    def fall(self) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
        """Gets the changed coordinates of the piece when it falls.

        Returns:
            Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
            Lists of old and new piece locations after the fall in the form ([(old_y1, old_x1), ...], [(new_y1, new_x1), ...]).
        """

        raise NotImplementedError


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


class TetrisPlayer:
    async def play_move(self, board: TetrisBoard) -> Action:
        raise NotImplementedError


class TetrisGameRunner:
    def __init__(self, agent: TetrisPlayer, seed: int = -1) -> None:
        self.seed = seed
        self.score = 0
        self.running = True
        self.agent = agent
        self.board = TetrisBoard()
        self.board.piece = TetrisPiece()

    def _handle_doxa_initialisation(self):
        """Synchronises with DOXA at the start of a game."""

        assert input() == "INIT"
        print("OK")

    def _handle_update(self, line):
        line_list = line.split(",")

        if line_list[0] == "LC":
            self.score = int(line_list[1])

            lines_to_clear = [int(line) for line in line_list[2:]]
            self.board.clear_lines(lines_to_clear)

        elif line_list[0] == "CHANGE":
            self.board.piece.piece_type = line_list[1]
            self.board.piece.x = int(line_list[2])
            self.board.piece.y = int(line_list[3])
            self.board.piece.orientation = int(line_list[4])

            updates = line_list[5:]
            for update in updates:
                split_update = update.split(".")
                self.board.board[int(split_update[1])][int(split_update[2])] = (
                    None if split_update[0] == "N" else split_update[0]
                )

        else:
            raise TypeError(
                f"Updates should be of Type LC or CHANGE, received {str(line_list[0])}"
            )

    async def run(self):
        self._handle_doxa_initialisation()

        while True:
            message = input()

            if message == "MOVE":
                action = await self.agent.play_move(self.board)

                action = action.numerator

                assert action in range(6)

                print(str(action))

            else:
                self._handle_update(message)
