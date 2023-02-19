import asyncio
from random import randrange

from tetris import Action, BaseAgent, Board, GameRunner

#################################################################
#   Modify the Agent class below to implement your own agent.   #
#   You may define additional methods as you see fit.           #
#################################################################


class Agent(BaseAgent):
    async def play_move(self, board: Board) -> Action:
        """Makes a Tetris move.

        Args:
            board (Board): The Tetris board.

        Returns:
            Action: The action to perform.
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
