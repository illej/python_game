import globals
from vector import Vector
from animator import Animator



class PositionAnimator(Animator):
    def __init__(self, entity):
        super().__init__(entity)
        self._original_position = Vector(entity.x, entity.y)
        self._destination = None
        self._elapsed_time = 0
        self._fps_interval = 1000 / globals.FPS
        self._movement_distance = 1.5
        self._movement_duration = 0.8

    def animate(self, delta):
        if delta < self._movement_duration and self._elapsed_time < self._movement_duration:
            self._elapsed_time += delta
            positional_delta = self._calc_positional_delta(delta,
                                                           self._movement_duration,
                                                           self._movement_distance)
            self._entity.positional_delta(positional_delta)
            self._entity.move()
        else:
            self._elapsed_time = 0

    def _calc_positional_delta(self, delta, movement_duration, movement_distance):
        percentage = delta / movement_duration
        return movement_distance * percentage


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)