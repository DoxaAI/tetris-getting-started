from random import randrange

from engine.actions import Action
from engine.board import TetrisBoard


class BaseAgent:
    async def play_move(self, board: TetrisBoard) -> Action:
        raise NotImplementedError


class Agent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()

    async def play_move(self, board: TetrisBoard) -> Action:
        raise NotImplementedError


class RandomAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()

    async def play_move(self, board: TetrisBoard) -> Action:
        return Action(randrange(6))


class HumanAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()

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
