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
        self._positional_delta = 0
        self._moves = 0
        self._is_moving = False

    def animate(self, delta):
        if self._elapsed_time < self._movement_duration and self._is_moving:
            self._elapsed_time += delta

            self._positional_delta = self._movement_distance * (delta / self._movement_duration)

            # self._x += self._directions[self._facing][0] * positional_delta
            # self._y += self._directions[self._facing][1] * positional_delta
            self._moves += 1
        else:
            self._elapsed_time = 0
            self._is_moving = False
            self._moves = 0

    @property
    def positional_delta(self):
        return self._positional_delta

    @property
    def is_moving(self):
        return self._is_moving

    @is_moving.setter
    def is_moving(self, value):
        self._is_moving = value


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)