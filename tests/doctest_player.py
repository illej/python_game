from .context import zelda_souls
from zelda_souls.player import Player
from zelda_souls.vector import Vector


def animate_01():
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


def animate_02():
    """
    >>> p = Player(Vector(2, 3))
    > segments: 3, segment_len: 0.035, anim_len: 0.10500000000000001 (seconds)
    >>> p._fps_interval
    33.333333333333336
    >>> p.update(0.033)
    Player state: 0
    >>> p._elapsed_time
    0.033
    >>> p.visual_representation
    (0, 0, 255)

    >>> p.update(0.033)
    Player state: 0
    >>> p._elapsed_time
    0.066
    >>> p.visual_representation
    (0, 0, 255)

    >>> p.update(0.033)
    Player state: 1
    >>> p._elapsed_time
    0
    >>> p.visual_representation
    (0, 255, 0)
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    animate_01()
    animate_02()