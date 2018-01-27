from entity import Entity
from vector import Vector
import colours


class Player(Entity):
    """
    >>> p = Player(Vector(2, 3))
    > segments: 3, segment_len: 1, anim_len: 3
    >>> p.update(0.01)
    Player state: 0
    >>> p._elapsed_time
    0.01
    >>> p.update(0.01)
    Player state: 0
    >>> p._elapsed_time
    0.02
    >>> p.visual_representation
    (0, 0, 255)
    >>> p.update(0.01)
    Player state: 0
    >>> p._elapsed_time
    0.03
    >>> p.visual_representation
    (0, 0, 255)
    >>> p.update(0.01)
    Player state: 1
    >>> p._elapsed_time
    0
    >>> p.visual_representation
    (0, 255, 0)
    """
    def __init__(self, vector):
        super().__init__(vector)
        self._speed = 1
        self._elapsed_time = 0
        self._fps_interval = 1000 / 30
        self._visual_representation_state = 0
        self._colours = {0: colours.BLUE,
                         1: colours.GREEN,
                         2: colours.RED}
        self._animation_segments = len(self._colours)
        self._animation_segment_length = 1  # seconds
        self._animation_length = self._animation_segments * self._animation_segment_length
        print('> segments: {}, segment_len: {}, anim_len: {}'.format(self._animation_segments,
                                                                     self._animation_segment_length,
                                                                     self._animation_length))

    def move_up(self):
        self._y -= self._speed

    def move_down(self):
        self._y += self._speed

    def move_left(self):
        self._x -= self._speed

    def move_right(self):
        self._x += self._speed

    @property
    def visual_representation(self):
        return self._get_colour(self._visual_representation_state)

    def _get_colour(self, state):
        return self._colours[state]

    def update(self, delta):
        # if delta < self._fps_interval and self._elapsed_time < self._fps_interval:
        if delta < self._animation_segment_length and self._elapsed_time < self._animation_segment_length:
            self._elapsed_time += delta
        else:
            self._visual_representation_state += 1
            self._elapsed_time = 0
            if self._visual_representation_state > len(self._colours):
                self._visual_representation_state = 0
        print('Player state: {}'.format(self._visual_representation_state))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)