from grid import Grid
import math
from vector import Vector
from entity import Entity
from player import Player


class World(object):
    def __init__(self, map, legend):
        self._map = map
        self._legend = legend
        self._grid = self._load()
        self._unit = 50
        self._populate_grid()
        self.player = self._get_player()

    def _load(self):
        width = len(self._map)
        height = len(self._map[0])

        print('w:', width)
        print('h:', height)

        grid = [['x' for y in range(width)] for x in range(height)]
        return grid

    def _populate_grid(self):
        for y in range(len(self._grid)):
            row = self._grid[y]
            for x in range(len(row)):
                self._grid[y][x] = self.element_from_char(self._legend,
                                                          self._map[y][x],
                                                          Vector(x * self._unit,
                                                                 y * self._unit))

    def _get_player(self):
        for y in range(len(self._grid)):
            for x in range(len(self._grid[0])):
                entity = self._grid[y][x]
                if isinstance(entity, Player):
                    return entity

    def get_entities(self):
        entities = []
        for y in range(len(self._grid)):
            for x in range(len(self._grid[0])):
                entity = self._grid[y][x]
                entities.append(entity)
        return entities

    def to_string(self):
        output = []
        for y in range(len(self._grid)):
            for x in range(len(self._grid[0])):
                element = self._grid[y][x]
                output.append(self.char_from_element(element))
            output.append('\n')
        return ''.join(output)

    def get_grid(self):
        return self._grid

    def element_from_char(self, legend, character, vector):
        if character is " ":
            return None
        element = legend[character](vector)
        element.origin_char = character
        return element

    def char_from_element(self, element):
        if element is None:
            return " "
        else:
            return element.origin_char

    def random_element(self, array):
        element = math.floor(math.random() * len(array))
        return array[element]