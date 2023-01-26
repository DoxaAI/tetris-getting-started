import asyncio
from random import randrange

from engine.board import TetrisBoard
from engine.game import (
    Action,
    BaseAgent,
    HumanAgent,
    LocalTetrisGame,
)
from engine.interfaces import TetrisCLI

from submission.tetris import TetrisPlayer
from submission.run import Agent


class RandomAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()

    async def play_move(self, board: TetrisBoard) -> Action:
        return Action(randrange(6))


async def main():
    agent = Agent()
    game = LocalTetrisGame(agent)

    ui = TetrisCLI(game, fast=False)
    await ui.run()


if __name__ == "__main__":
    asyncio.run(main())
