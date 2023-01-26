import os
import time

import click

from engine.board import TetrisBoard
from engine.game import LocalTetrisGame


class TetrisUI:
    def __init__(self, game: LocalTetrisGame) -> None:
        self.game = game

    async def run(self) -> None:
        raise NotImplementedError


class TetrisCLI(TetrisUI):
    chars = {
        None: "\033[249m - \033[0m",
        "I": "\033[96m ■ \033[0m",
        "O": "\033[93m ■ \033[0m",
        "S": "\033[92m ■ \033[0m",
        "Z": "\033[91m ■ \033[0m",
        "L": "\033[38;5;208m ■ \033[0m",
        "J": "\033[94m ■ \033[0m",
        "T": "\033[95m ■ \033[0m",
    }

    def __init__(self, game: LocalTetrisGame, fast: bool = False) -> None:
        super().__init__(game)

        self.fast = fast

    def print_board(self, board: TetrisBoard, score: int) -> None:
        os.system("cls")
        for row in board.board:
            print("".join(self.chars[cell] for cell in row))

        click.echo(f"\n {click.style('Score', bold=True)}: {score}\n")
        time.sleep(0.4)

    async def run(self) -> None:
        async for running, score, board, action in self.game.run():
            if not running:
                break

            if not self.fast or action is None:
                self.print_board(board, score)


class TetrisDOXARunner:
    pass
