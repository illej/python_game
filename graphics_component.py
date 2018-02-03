class GraphicsComponent(object):
    def __init__(self):
        self._sprite_stand = None
        self._sprite_walk_left = None
        self._sprite_walk_right = None

    def update(self, actor, graphics):
        sprite = self._sprite_stand

        if actor.velocity < 0:
            sprite = self._sprite_walk_left
        elif actor.velocity > 0:
            sprite = self._sprite_walk_right

        graphics.draw(sprite, actor.x, actor.y)