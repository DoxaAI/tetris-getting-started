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

The `play_move()` method should return one of the following actions:

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
