from __future__ import annotations
from typing import List, Dict, Tuple, Optional
from enum import IntEnum
import copy
import numpy as np

"""
This file contains code for defining a representation of a player of the
iterated prisoner's dilemma game and for interfacing with DOXA.
For the most part, you will not need to modify this module at all. Instead,
create your own agent in `run.py` by implementing the `play_move` method.
You may add additional methods as you see fit!
The directory you submit to DOXA must contain all the files necessary to
run your agent, including any machine learning models. Please do not include
any files that are not related to your current submission.
"""


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


class TetrisPlayer:
    def play_move(self, board: TetrisBoard) -> Action:
        raise NotImplementedError


class TetrisGameRunner:
    def __init__(self, agent: TetrisPlayer, seed: int = -1) -> None:
        self.seed = seed
        self.score = 0
        self.running = True
        self.agent = agent
        self.board = TetrisBoard()

    def _handle_doxa_initialisation(self):
        """Synchronises with DOXA at the start of a game."""

        assert input() == "INIT"
        print("OK")

    def _handle_update(self):
        line = input()

        line_list = line.split(".")

        self.score = int(line_list[0])
        self.board.piece.piece_type = line_list[1]
        self.board.piece.x = int(line_list[2])
        self.board.piece.y = int(line_list[3])
        self.board.piece.orientation = int(line_list[4])
        board_state = line_list[5]

        board_updates = board_state.split(",")

        self.board.board = [[None] * 10 for _ in range(21)]

        pointer = 0
        while board_updates[pointer] != "":
            self.board.board[int(board_updates[pointer + 1])][
                int(board_updates[pointer + 2])
            ] = str(board_updates[pointer])
            pointer += 3

    def run(self):
        self._handle_doxa_initialisation()

        while True:
            self._handle_update()

            action = self.agent.play_move(self.board).numerator

            assert action in range(6)

            print(str(action))
