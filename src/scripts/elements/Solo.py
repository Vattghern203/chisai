from typing import List

from scripts.elements.Object import Object

class Terrain:

    def __init__(self, position:List[int, int], block_width:int | float, block_height:int | float, length: int) -> None:
        
        self.block_width = block_width
        self.block_height = block_height | block_width
        self.position = position
        self.length = length

            