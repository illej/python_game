class PhysicsComponent(object):
    def __init__(self):
        self._volume = None

    def update(self, actor, world):
        actor.x += actor.velocity
        world.resolve_collision(self._volume, actor.x, actor.y, actor.velocity)