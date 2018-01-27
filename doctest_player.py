from player import Player
from vector import Vector


def animate_low_delta():
    """
    >>> p = Player(Vector(2, 3))
    > segments: 3, segment_len: 1000, anim_len: 3000
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


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    animate_low_delta()