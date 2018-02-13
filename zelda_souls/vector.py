class Vector(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def plus(self, other):
        return Vector(self._x + other.x,
                      self._y + other.y)