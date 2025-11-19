from typing import Tuple, Dict, Literal

Direction = Literal['Right', 'Down', 'Left', 'Up']
Coord = Tuple[int, int]
Body = Dict[Coord, Direction]