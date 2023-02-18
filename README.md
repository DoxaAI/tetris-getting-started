# Getting Started with Tetris on DOXA

Here is everything you need to get started with the Tetris competition on DOXA! There is also more information available on the [DOXA Tetris competition page](https://doxaai.com/competition/tetris).

Feel free to fork this repository and use it as the base for implementing your own agents! You can also join the conversation on the [DOXA Discord server](https://discord.gg/MUvbQ3UYcf).

## Prerequisites

Before you begin, pleasure ensure you have Python 3.9+ and the DOXA CLI installed.

If you do not yet have the DOXA CLI installed, you may do so with `pip`:

```bash
pip install doxa-cli
```

You should also install the dependencies in `requirements.txt`:

```bash
pip install -r requirements.txt
```

You can also take advantage of TensorFlow to create a reinforcement learning agent! This is completely optional, but if you'd like to, you can install TensorFlow too:

```bash
pip install tensorflow
```

## Running the Tetris Engine Locally

The `engine` directory contains the code for the game engine, which you can run from the root directory with:

```bash
python -m engine
```

## What's in the Engine?

`actions.py` contains the list of actions that your agent should return one of.

`agents.py` contains the classes of default agents provided, and an agent you can implement to test locally.

`board.py` contains the `TetrisBoard` class code base.

`game.py` contains the code to run a game of Tetris locally.

`interfaces.py` contains the code for the interfaces that are supported.

`piece.py` and the `pieces` directory contain the classes for each Tetromino.

## What can you do with the Tetris Engine?

You can implement the `play_move()` function of the `Agent` class in `agents.py` if you'd like to run your agent locally. We advise developing your agent here before copying it to the submission directory (further details below).

You'll also notice that `agents.py` contains the code for a random agent, as well as a human agent so you can play Tetris too. Please note that the human agent does not currently work with the PyGame interface.

You can edit the `__main__.py` file to change the agent and interface you'd like to use. You can change line 7 to be any agent in `agents.py`. By default, this is set to the random agent. You can also change the interface by switching the comments on lines 14 and 15. By default this is set to the PyGame interface. Please don't edit anything else in this file, otherwise you may not be able to properly run Tetris locally!

## Implementing an Agent

First, clone this repository if you have not already done so. Then, you can start implementing your first agent by modifying the `play_move()` method of the agent in `run.py` in the `submission` directory. As stated above, you can develop your agent in `engine/agents.py`, then copy contents of `play_move()` over to the submission directory.

By default, the agent just plays moves at random. What interesting strategies can you come up with? 👀

## Submitting to DOXA

Before you can submit your agent to DOXA, you must first ensure that you are logged into the DOXA CLI. You can do so with the following command:

```bash
doxa login
```

Then, when you are ready to submit your agent (contained within the `submission` folder) to DOXA, run the following command from the root directory:

```bash
doxa upload submission
```

Please ensure that the `submission` folder only contains the files you wish to upload to DOXA. If you have renamed your submission folder to something else, substitute `submission` for the new folder name.