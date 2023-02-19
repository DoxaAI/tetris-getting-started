from typing import Sequence, Union

from tetris.board import Action, Board


class BaseAgent:
    async def play_move(self, board: Board) -> Union[Action, Sequence[Action]]:
        raise NotImplementedError
