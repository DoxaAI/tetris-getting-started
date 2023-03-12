import asyncio
import math
import os
import sys
import time
from io import BytesIO

import pygame
import requests
from PIL import Image
from pygame.locals import KEYDOWN, K_a, K_d, K_e, K_q, K_s

sys.path.append(os.path.dirname(os.path.abspath("submission/tetris")))

from tetris.agent import BaseAgent
from tetris.board import Action, Board
from tetris.constants import BOARD_HEIGHT, BOARD_WIDTH
from tetris.game import Game
from tetris.interface import TetrisUI

PIECE_COLOURS = {
    None: (100, 100, 100),  # GREY
    "I": (0, 255, 255),  # CYAN
    "J": (0, 0, 255),  # BLUE
    "L": (255, 127, 0),  # ORANGE
    "O": (255, 255, 0),  # YELLOW
    "S": (0, 255, 0),  # GREEN
    "Z": (255, 0, 0),  # RED
    "T": (186, 33, 209),  # PURPLE
}


class TetrisPygame(TetrisUI):
    def __init__(self, pause_time: float = 0.1) -> None:
        super().__init__()

        self.pause_time = pause_time

        pygame.init()

        self._clock = pygame.time.Clock()
        self._display = pygame.display.Info()
        self._screen = pygame.display.set_mode(
            [int(self._display.current_w * 0.21), int(self._display.current_h * 0.65)]
        )
        self._score_font = pygame.font.Font("freesansbold.ttf", 26)

        self.CELL_HEIGHT = self.CELL_WIDTH = math.ceil(self._display.current_w * 0.012)
        self.CELL_MARGIN = math.ceil(self._display.current_w * 0.0005)

    def setup(self) -> None:
        """Performs the Pygame setup for Tetris."""

        try:
            # Try fetching the logo as the icon for the Pygame window
            logo = Image.open(
                BytesIO(requests.get("https://doxaai.com/logo.png").content)
            ).convert("RGBA")

            icon = pygame.image.fromstring(logo.tobytes(), logo.size, logo.mode)
            pygame.display.set_icon(icon)
        except:
            pass

        pygame.display.set_caption("Tetris")

    def render(self, board: Board, score: int) -> None:
        """Renders the PyGame window with the current board state and score.

        Args:
            board (Board): The current board state.
            score (int): The current score of the game.
        """

        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                # Draw the current cell
                pygame.draw.rect(
                    self._screen,
                    PIECE_COLOURS[board.board[y][x]],
                    [
                        (self.CELL_MARGIN + self.CELL_WIDTH) * x
                        + self.CELL_MARGIN
                        + math.floor(self._display.current_w * 0.038),
                        (self.CELL_MARGIN + self.CELL_HEIGHT) * y
                        + self.CELL_MARGIN
                        + math.floor(self._display.current_h * 0.1),
                        self.CELL_WIDTH,
                        self.CELL_HEIGHT,
                    ],
                )

        # Render the text for the score
        text = self._score_font.render(f"Score: {score}", True, (255, 255, 255))

        text_rectangle = text.get_rect()
        text_rectangle.center = (
            math.floor(self._display.current_w * 0.104),
            math.floor(self._display.current_h * 0.05),
        )

        self._screen.blit(text, text_rectangle)

    def has_quit(self) -> None:
        """Checks whether the user has exited the PyGame window."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

        return False

    async def run(self, game: Game) -> None:
        """Runs the game for the Pygame UI."""

        self.setup()

        async for changes, cleared_lines, board, action in game.run():
            self._screen.fill((0, 0, 0))

            # Exit if exit button is pressed during the game
            if self.has_quit():
                break

            self.render(board, game.score)

            time.sleep(self.pause_time)
            self._clock.tick(60)

            pygame.display.flip()

        else:
            # Wait for the user to exit at the end of the game
            while not self.has_quit():
                continue

        pygame.quit()


class HumanAgent(BaseAgent):
    async def play_move(self, board: Board) -> Action:
        move = pygame.event.wait()
        while move.type != KEYDOWN and move.type != pygame.QUIT:
            move = pygame.event.wait()

        if move.type == pygame.QUIT:
            pygame.quit()

        if move.type == KEYDOWN:
            if move.key == K_q:
                return Action.ROTATE_ANTICLOCKWISE
            elif move.key == K_e:
                return Action.ROTATE_CLOCKWISE
            elif move.key == K_a:
                return Action.MOVE_LEFT
            elif move.key == K_d:
                return Action.MOVE_RIGHT
            elif move.key == K_s:
                return Action.HARD_DROP

            return Action.NOOP


async def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--live":
        agent = HumanAgent()
    else:
        from submission.agent import SelectedAgent  # your agent

        agent = SelectedAgent()

    ui = TetrisPygame()
    await ui.run(Game(agent))


if __name__ == "__main__":
    asyncio.run(main())
