from entity import Entity


class Wall(Entity):
    def __init__(self, vector):
        super().__init__(vector)