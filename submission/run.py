from typing import Literal
from random import randrange

from tetris import (
    TetrisGameRunner,
    TetrisPlayer,
    TetrisBoard,
    TetrisPiece,
    Action,
)


class Agent(TetrisPlayer):
    def __init__(self) -> None:
        super().__init__()

    def play_move(self, board: TetrisBoard) -> Action:
        return Action(randrange(6))


#####################################################################
#   This runs your agent and communicates with DOXA over stdio,     #
#   so please do not touch these lines unless you are comfortable   #
#   with how DOXA works, otherwise your agent may not run.          #
#####################################################################

if __name__ == "__main__":
    agent = Agent()

    TetrisGameRunner(agent).run()
