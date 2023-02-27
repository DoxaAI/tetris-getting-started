from typing import Dict, List, Optional, Tuple

BoardState = List[List[Optional[str]]]
Cell = Tuple[int, int]

LINE_CLEAR_SCORES: Dict[int, int] = {1: 100, 2: 250, 3: 750, 4: 3000}

BOARD_WIDTH: int = 10
BOARD_HEIGHT: int = 21
