from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    def __init__(self, vector):
        self._x = vector.x
        self._y = vector.y
        self._origin_char = None
        self._visual_representation = None

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def origin_char(self):
        return self._origin_char

    @origin_char.setter
    def origin_char(self, char):
        self._origin_char = char

    @property
    def visual_representation(self):
        return self._visual_representation