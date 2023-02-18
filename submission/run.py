import asyncio
from random import randrange

from tetris import (
    TetrisGameRunner,
    TetrisPlayer,
    TetrisBoard,
    TetrisPiece,
    Action,
)

#################################################################
#   Modify the Agent class below to implement your own agent.   #
#   Implement the play_move function to return an Action.       #
#   You may define additional methods as you see fit.           #
#################################################################


class Agent(TetrisPlayer):
    def __init__(self) -> None:
        super().__init__()

    async def play_move(self, board: TetrisBoard) -> Action:
        return Action(randrange(6))


#####################################################################
#   This runs your agent and communicates with DOXA over stdio,     #
#   so please do not touch these lines unless you are comfortable   #
#   with how DOXA works, otherwise your agent may not run.          #
#####################################################################

if __name__ == "__main__":
    agent = Agent()

    asyncio.run(TetrisGameRunner(agent).run())
