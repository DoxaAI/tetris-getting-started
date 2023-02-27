from typing import Dict, List, Type

from tetris.piece import Piece
from tetris.pieces.i import IPiece
from tetris.pieces.j import JPiece
from tetris.pieces.l import LPiece
from tetris.pieces.o import OPiece
from tetris.pieces.s import SPiece
from tetris.pieces.t import TPiece
from tetris.pieces.z import ZPiece

PIECES: List[Type[Piece]] = [
    OPiece,
    IPiece,
    SPiece,
    ZPiece,
    LPiece,
    JPiece,
    TPiece,
]

PIECE_MAPPINGS: Dict[str, Type[Piece]] = {
    "I": IPiece,
    "J": JPiece,
    "L": LPiece,
    "O": OPiece,
    "S": SPiece,
    "T": TPiece,
    "Z": ZPiece,
}
