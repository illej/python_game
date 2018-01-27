from entity import Entity
from vector import Vector
import colours
import globals
from colour_animator import ColourAnimator


class Player(Entity):
    """
    >>> p = Player(Vector(2, 3))
    > segments: 3, segment_len: 0.035, anim_len: 0.10500000000000001 (seconds)
    >>> p._fps_interval
    33.333333333333336
    >>> p.update(0.01)
    Player state: 0
    >>> p._elapsed_time
    0.01
    >>> p.visual_representation
    (0, 0, 255)

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
    Player state: 0
    >>> p._elapsed_time
    0.04
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
        self._colours = {0: colours.BLUE,
                         1: colours.GREEN,
                         2: colours.RED}
        self._animator = ColourAnimator(self._colours)

    def handle_input(self, user_input):
        # TODO: stuff about states
        pass

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
        return self._animator.current_colour

    def update(self, delta):
        self._animator.animate(delta)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)