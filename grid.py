from vector import Vector


class Grid(object):
    """
    >>> g = Grid(2, 2)
    >>> g.make_space()
    [[-1, -1], [-1, -1]]
    >>> g.make_space_better()
    [[-1, -1], [-1, -1]]
    """
    def __init__(self, w, h):
        self._width = w
        self._height = h
        self._filler_tile = '-'
        self._space = self.make_space_better()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        self._height = h

    def get(self, vector):
        row = self._space[vector.y]
        column = row[vector.x]
        return column

    def set(self, vector, value):
        self._space[vector.y][vector.x] = value

    # old
    def make_space(self):
        twod_list = []
        for y in range(self._height):
            new = []
            for x in range(self._width):
                new.append(self._filler_tile)
            twod_list.append(new)
        return twod_list

    def make_space_better(self):
        return [[self._filler_tile for y in range(self._width)] for x in range(self._height)]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)