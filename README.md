# Getting Started with Tetris on DOXA

This repository contains everything you need to get started with Tetris on DOXA. For more information, check out the [competition page](https://doxaai.com/competition/tetris). 😎

Feel free to fork this repository and use it as the foundation for your own agents. You can also join the conversation on the [DOXA Community Discord server](https://discord.gg/MUvbQ3UYcf). 👀

## Prerequisites

Before you begin, please ensure that you have Python 3.9+ and the DOXA CLI installed.

If you do not yet have the DOXA CLI installed, you may do so using `pip`:

```bash
pip install -U doxa-cli
```

Installing the DOXA CLI will also install the `click` package used by the Tetris CLI.

**Note**: on macOS and some flavours of Linux, you may have to use `python3 -m pip` or `pip3` instead of just plain `pip`.

If you wish to use the PyGame-based UI, you will also need to install the following packages:

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
- `gui.py`: a PyGame-based GUI for running your Tetris agent (run with `python gui.py`)
- `Pipfile`: a Pipfile to install dependencies with `pipenv`

## Implementing an agent

First, clone this repository if you have not already done so. You can then start implementing your first agent by modifying the `play_move()` method of the agent in `submission/agent.py`.

The `play_move()` method receives the current Tetris board (`board`) as an argument and should return either a single `Action` or a sequence (i.e. a list) of actions, which will be performed in turn until the piece lands (at which point any remaining actions are discarded).

The Tetris `Board` object (passed in as `board`) has a number of useful attributes:
- `board.board`: the current state of the Tetris board represented as a list of lists, where each inner list corresponds to a row. Note that our Tetris board has 21 rows and 10 columns, rather than only 20 rows, with the extra hidden row at index `0` serving as a buffer for rotations directly after pieces spawn.
- `board.piece`: The current Tetris piece dropping down that you are controlling.
- `board.piece.piece_type`: The type of the current Tetris piece. It can be one of `I`, `J`, `L`, `O`, `S`, `T` or `Z`.

The board also exposes the `with_move()` and `with_moves()` methods, which return a copy of the board with the provided action or actions applied to the board, respectively.

Actions are defined as follows:

```py
class Action(IntEnum):
    NOOP = 0    # no operation
    ROTATE_ANTICLOCKWISE = 1
    ROTATE_CLOCKWISE = 2
    MOVE_LEFT = 3
    MOVE_RIGHT = 4
    HARD_DROP = 5
```

By default, the agent just plays moves at random. What interesting gameplay strategies can you come up with? 👀

If you are curious as to how our implementation of Tetris works, take a look at the files in the `submission/tetris` directory.

## Running Tetris locally

You can see how your agent (as defined in `submission/agent.py`) performs locally using the CLI and GUI scripts provided.

Assuming you have the relevant packages installed as described above, to launch the PyGame-based GUI, run the following command from the root of this repository:

```bash
python gui.py
```

**Note**: on macOS and some flavours of Linux, use `python3` instead of `python`.

To launch the Tetris CLI script, run the following command from the root of this repository:

```bash
python cli.py
```

### Playing the game yourself

You can also play the game yourself using either one of the CLI or GUI scripts by specifying the `--live` flag.

```bash
python gui.py --live
```

```bash
python cli.py --live
```

The controls are as follows:
- `q`: `ROTATE_ANTICLOCKWISE`
- `e`: `ROTATE_CLOCKWISE`
- `a`: `MOVE_LEFT`
- `d`: `MOVE_RIGHT`
- `s`: `HARD_DROP`
- Anything else: `NOOP`

**Note**: in the CLI, you need to hit `ENTER` after each move.

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
