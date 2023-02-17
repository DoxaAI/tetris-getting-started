import asyncio

from engine.agents import *
from engine.game import TetrisGame
from engine.interfaces import TetrisCLI, TetrisPygame

SelectedAgent = RandomAgent


async def main():
    agent = SelectedAgent()
    game = TetrisGame(agent)

    # ui = TetrisCLI(game, fast=False)
    ui = TetrisPygame(game)
    await ui.run()


if __name__ == "__main__":
    asyncio.run(main())
