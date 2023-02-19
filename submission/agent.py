import asyncio
from random import randrange
from typing import Sequence, Union

from tetris import Action, BaseAgent, Board, GameRunner

#################################################################
#   Modify the Agent class below to implement your own agent.   #
#   You may define additional methods as you see fit.           #
#################################################################


class Agent(BaseAgent):
    async def play_move(self, board: Board) -> Union[Action, Sequence[Action]]:
        """Makes at least one Tetris move.

        If a sequence of moves is returned, they are made in order
        until the piece lands (with any remaining moves discarded).

        Args:
            board (Board): The Tetris board.

        Returns:
            Union[Action, Sequence[Action]]: The action(s) to perform.
        """

        # Perform a random action
        return Action(randrange(6))


SelectedAgent = Agent

#####################################################################
#   This runs your agent and communicates with DOXA over stdio,     #
#   so please do not touch these lines unless you are comfortable   #
#   with how DOXA works, otherwise your agent may not run.          #
#####################################################################

if __name__ == "__main__":
    agent = SelectedAgent()

    asyncio.run(GameRunner(agent).run())
