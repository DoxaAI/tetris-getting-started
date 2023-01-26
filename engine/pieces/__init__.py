from typing import List, Type

from engine.piece import TetrisPiece
from engine.pieces.i import IPiece
from engine.pieces.j import JPiece
from engine.pieces.l import LPiece
from engine.pieces.o import OPiece
from engine.pieces.s import SPiece
from engine.pieces.t import TPiece
from engine.pieces.z import ZPiece

PIECES: List[Type[TetrisPiece]] = [
    OPiece,
    IPiece,
    SPiece,
    ZPiece,
    LPiece,
    JPiece,
    TPiece,
]
