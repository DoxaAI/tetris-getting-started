# Getting Started with Tetris on DOXA

This repository contains everything you need to get started with Tetris on DOXA. For more information, check out the [competition page](https://doxaai.com/competition/tetris). 😎

Feel free to fork this repository and use it as the foundation for your own agents. You can also join the conversation on the [DOXA Community Discord server](https://discord.gg/MUvbQ3UYcf).

## Prerequisites

Before you begin, please ensure that you have Python 3.9+ and the DOXA CLI installed.

If you do not yet have the DOXA CLI installed, you may do so using `pip`:

```bash
pip install -U doxa-cli
```

If you wish to use the Pygame-based UI, you will also need to install the following packages:

```bash
pip install pygame pillow requests
```

If you would rather use `Pipenv` to install and set everything up, run the following commands:

```bash
pipenv install
pipenv shell
```

## Repository structure

- `submission/`: the directory that gets uploaded to DOXA
    - `submission/tetris/`: this module contains a full implementation of Tetris
    - `submission/agent.py`: this is where you should implement your own agent!
    - `submission/doxa.yaml`: this is a configuration file used by DOXA to handle your submission
- `cli.py`: a CLI for running your Tetris agent (run with `python cli.py`)
- `gui.py`: a Pygame-based GUI for running your Tetris agent (run with `python gui.py`)
- `Pipfile`: a Pipfile to install dependencies with `pipenv`

## Implementing an agent

First, clone this repository if you have not already done so. Then, you can start implementing your first agent by modifying the `play_move()` method of the agent in `submission/agent.py`.

The current state of the Tetris board, `board`, is an argument to the `play_move()` method. This object contains all the information you'll need to decide an action to take. Feel free to take a look through the files in `submission/tetris` if you'd like to, but the most relevant information you'll need is:

- `board.board`: a 2D list containing the current state of the Tetris board. Please note there is an extra row at index `[0]` (the top of the board) that you can exclude from any algorithms you may write. This row serves as a buffer for rotations directly after pieces spawn.

- `board.piece`: The current Tetris piece that you are controlling.

- `board.piece.piece_type`: The type of the current Tetris piece. It can be one of: `{I, J, L, O, S, T, Z}`.

The `play_move()` method should return at least one of the following actions:

```py
class Action(IntEnum):
    NOOP = 0    # no operation
    ROTATE_ANTICLOCKWISE = 1
    ROTATE_CLOCKWISE = 2
    MOVE_LEFT = 3
    MOVE_RIGHT = 4
    HARD_DROP = 5
```

You can also return a sequence (e.g. a list) of moves, which will be performed in order until the piece lands (at which point any remaining moves are discarded).

By default, the agent just plays moves at random. What interesting gameplay strategies can you come up with? 👀

## Running Tetris locally

You can run Tetris locally to either view your agent in action, or play the game yourself!

Run `python cli.py` from the root directory to view the game in the command line. If you have PyGame installed, you can run `python gui.py` instead for some fancier graphics. Both of these will use the agent you've implemented.

If you'd like to play Tetris yourself, you can add `--live` to either one of the commands above, e.g., `python gui.py --live`. The controls are:

```
q: ROTATE_ANTICLOCKWISE
e: ROTATE_CLOCKWISE
a: MOVE_LEFT
d: MOVE_RIGHT
s: HARD_DROP
anything else: NOOP
```

## Submitting to DOXA

Before you can submit your agent to DOXA, you must first ensure that you are logged into the DOXA CLI. You can do so with the following command:

```bash
doxa login
```

You should also make sure that you are enrolled on the [Tetris competition page](https://doxaai.com/competition/tetris).

Then, when you are ready to submit your agent (contained within the `submission` directory) to DOXA, run the following command from the root of the repository:

```bash
doxa upload submission
```

Please ensure that the `submission` directory only contains the files you wish to upload to DOXA. If you have renamed your submission directory to something else, substitute `submission` for the new directory name.
