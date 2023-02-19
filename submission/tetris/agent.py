from tetris.board import Action, Board


class BaseAgent:
    async def play_move(self, board: Board) -> Action:
        raise NotImplementedError
