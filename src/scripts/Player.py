from scripts.Entity import Entity


class Player(Entity):

    def __init__(self, x: int, y: int, width: float, height: float):
        super().__init__(x, y, width, height)


    