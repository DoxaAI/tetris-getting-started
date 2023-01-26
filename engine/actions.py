from enum import IntEnum


class Action(IntEnum):
    NOOP = 0
    ROTATE_ANTICLOCKWISE = 1
    ROTATE_CLOCKWISE = 2
    MOVE_LEFT = 3
    MOVE_RIGHT = 4
    HARD_DROP = 5
