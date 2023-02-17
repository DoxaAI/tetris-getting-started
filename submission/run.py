from tetris import (
    TetrisGameRunner,
    TetrisPlayer,
    TetrisBoard,
    Action,
)


class Agent(TetrisPlayer):
    def __init__(self) -> None:
        super().__init__()

    async def play_move(self, board: TetrisBoard) -> Action:
        raise NotImplementedError("No agent implemented!")


#####################################################################
#   This runs your agent and communicates with DOXA over stdio,     #
#   so please do not touch these lines unless you are comfortable   #
#   with how DOXA works, otherwise your agent may not run.          #
#####################################################################

if __name__ == "__main__":
    agent = Agent()

    TetrisGameRunner(agent).run()
