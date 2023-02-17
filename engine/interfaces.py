import os
import time
from io import BytesIO
import math

import click
import pygame
import requests
from PIL import Image

from engine.board import TetrisBoard
from engine.game import TetrisGame


class TetrisUI:
    def __init__(self, game: TetrisGame) -> None:
        self.game = game

    async def run(self) -> None:
        raise NotImplementedError


class TetrisCLI(TetrisUI):
    # Map the values to their respective colours
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

    def __init__(self, game: TetrisGame, fast: bool = False) -> None:
        super().__init__(game)

        self.fast = fast

    def print_board(self, board: TetrisBoard, score: int) -> None:
        """Prints the fancy CLI board.

        Args:
            board (TetrisBoard), score (int): The board to print and the current score.
        """

        # Clear current terminal output
        os.system("cls")

        # Print the board
        for row in board.board:
            print("".join(self.chars[cell] for cell in row))

        # Print the score
        click.echo(f"\n {click.style('Score', bold=True)}: {score}\n")
        time.sleep(0.1)

    async def run(self) -> None:
        """Runs the game for the CLI UI."""

        async for changes, score, board, action in self.game.run():
            if not self.game.running:
                break

            if not self.fast or action is None:
                self.print_board(board, score)


class TetrisPygame(TetrisUI):
    # Map the values to their respective colours
    colour_dict = {
        "N": (100, 100, 100),  # GREY
        "I": (0, 255, 255),  # CYAN
        "J": (0, 0, 255),  # BLUE
        "L": (255, 127, 0),  # ORANGE
        "O": (255, 255, 0),  # YELLOW
        "S": (0, 255, 0),  # GREEN
        "Z": (255, 0, 0),  # RED
        "T": (186, 33, 209),  # PURPLE
    }

    def __init__(self, game: TetrisGame, pause_time: float = 0.1) -> None:
        super().__init__(game)

        pygame.init()

        self.pause_time = pause_time

        # Set PyGame related values
        self.screenObj = pygame.display.Info()

        self.screen = pygame.display.set_mode(
            [self.screenObj.current_w * 0.2, self.screenObj.current_h * 0.65]
        )

        self.CELL_WIDTH, self.CELL_HEIGHT, self.CELL_MARGIN = (
            math.ceil(self.screenObj.current_w * 0.012),
            math.ceil(self.screenObj.current_w * 0.012),
            math.ceil(self.screenObj.current_w * 0.0005),
        )

        self.score_font = pygame.font.Font("freesansbold.ttf", 26)

        self.clock = pygame.time.Clock()

    def setup(self) -> None:
        """Performs the PyGame setup for Tetris."""

        try:
            # Try fetching the logo as the icon for the PyGame window

            logo = Image.open(
                BytesIO(requests.get("https://doxaai.com/logo.png").content)
            ).convert("RGBA")

            icon = pygame.image.fromstring(logo.tobytes(), logo.size, logo.mode)

            pygame.display.set_icon(icon)
        except:
            pass

        pygame.display.set_caption("Tetris!")

    async def run(self) -> None:
        """Runs the game for the PyGame UI."""

        self.setup()

        done = False

        async for changes, lines_to_clear, board, action in self.game.run():
            self.screen.fill((0, 0, 0))

            # Exit if exit button is pressed during the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    break

            if done:
                break

            for y in range(len(board.board)):
                for x in range(len(board.board[0])):
                    # Set the colour of the current cell
                    if not board.board[y][x]:
                        colour = self.colour_dict["N"]
                    else:
                        colour = self.colour_dict[board.board[y][x]]

                    # Draw the current cell
                    pygame.draw.rect(
                        self.screen,
                        colour,
                        [
                            (self.CELL_MARGIN + self.CELL_WIDTH) * x
                            + self.CELL_MARGIN
                            + math.floor(self.screenObj.current_w * 0.038),
                            (self.CELL_MARGIN + self.CELL_HEIGHT) * y
                            + self.CELL_MARGIN
                            + math.floor(self.screenObj.current_h * 0.1),
                            self.CELL_WIDTH,
                            self.CELL_HEIGHT,
                        ],
                    )

            # Render the text for the score
            text = self.score_font.render(
                f"Score: {self.game.score}", True, (255, 255, 255)
            )

            text_rect = text.get_rect()

            text_rect.center = (
                math.floor(self.screenObj.current_w * 0.10),
                math.floor(self.screenObj.current_h * 0.05),
            )

            self.screen.blit(text, text_rect)

            time.sleep(self.pause_time)

            self.clock.tick(60)
            pygame.display.flip()

        # When game is done, wait until the exit button is pressed
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    break

        pygame.quit()
