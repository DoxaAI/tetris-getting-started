from tetris.agent import BaseAgent
from tetris.board import Action, Board
from tetris.pieces import PIECE_MAPPINGS


class GameRunner:
    def __init__(self, agent: BaseAgent, seed: int = -1) -> None:
        self.seed = seed
        self.score = 0
        self.running = True
        self.agent = agent
        self.board = Board()

    def _handle_doxa_initialisation(self) -> None:
        """Synchronises with DOXA at the start of a game."""

        assert input() == "INIT"
        print("OK")

    async def run(self) -> None:
        """Communicates with DOXA to run a Tetris game.

        Raises:
            ValueError: An unknown message was received.
        """

        self._handle_doxa_initialisation()

        while True:
            message = input().split(" ")

            if not message:
                continue
            elif message[0] == "M":
                actions = await self.agent.play_move(self.board)
                if isinstance(actions, Action):
                    assert actions in Action
                    print(actions.value)
                elif actions:
                    print(*[action.value for action in actions])
                else:
                    print(Action.NOOP.value)
            elif message[0] == "L":
                self.score = int(message[1])
                self.board.clear_lines([int(line) for line in message[2:]])
            elif message[0] == "U":
                if not self.board.piece or self.board.piece.piece_type != message[1]:
                    self.board.piece = PIECE_MAPPINGS[message[1]]()

                self.board.piece.x = int(message[2])
                self.board.piece.y = int(message[3])
                self.board.piece.orientation = int(message[4])

                for update in message[5:]:
                    piece_type, y, x = update.split(",")
                    self.board.board[int(y)][int(x)] = (
                        None if piece_type == "N" else piece_type
                    )
            else:
                raise ValueError(f"Unknown message type: {message[0]}.")
