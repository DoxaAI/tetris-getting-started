import asyncio
import os
import sys
import time

import click

sys.path.append(os.path.dirname(os.path.abspath("submission/tetris")))

from tetris import Action, BaseAgent, Board
from tetris.game import Game
from tetris.interface import TetrisUI

CLEAR_COMMAND = "cls" if os.name == "nt" else "clear"

PIECES = {
    None: "\033[249m - \033[0m",
    "I": "\033[96m ■ \033[0m",
    "O": "\033[93m ■ \033[0m",
    "S": "\033[92m ■ \033[0m",
    "Z": "\033[91m ■ \033[0m",
    "L": "\033[38;5;208m ■ \033[0m",
    "J": "\033[94m ■ \033[0m",
    "T": "\033[95m ■ \033[0m",
}


class TetrisCLI(TetrisUI):
    def __init__(self, fast: bool = False) -> None:
        super().__init__()

        self.fast = fast

    def print_board(self, board: Board, score: int) -> None:
        """Displays the board.

        Args:
            board (Board): The board to print.
            score (int): The current score.
        """

        # Clear current terminal output
        os.system(CLEAR_COMMAND)

        # Print the board
        for row in board.board[1:]:
            print(*(PIECES[cell] for cell in row), sep="")

        # Print the score
        click.echo(f"\n {click.style('Score', bold=True)}: {score}\n")
        time.sleep(0.4)

    async def run(self, game: Game) -> None:
        """Runs the game for the CLI UI."""

        async for changes, cleared_lines, board, action in game.run():
            if not self.fast or action is None:
                self.print_board(board, game.score)


class HumanAgent(BaseAgent):
    async def play_move(self, board: Board) -> Action:
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


async def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--live":
        agent = HumanAgent()
    else:
        from submission.agent import SelectedAgent  # your agent

        agent = SelectedAgent()

    ui = TetrisCLI(fast=False)
    await ui.run(Game(agent))


if __name__ == "__main__":
    asyncio.run(main())
