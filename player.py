from entity import Entity
import colours
from directions import *
from colour_animator import ColourAnimator
from position_animator import PositionAnimator
import pygame
from pygame.locals import *


class Player(Entity):
    def __init__(self, vector):
        super().__init__(vector)
        self._speed = 50
        self._colours = {0: colours.BLUE,
                         1: colours.GREEN,
                         2: colours.RED}
        self._moves = {UP: self.move_up,
                       DOWN: self.move_down,
                       LEFT: self.move_left,
                       RIGHT: self.move_right}
        self._facing = DOWN
        self._colour_animator = ColourAnimator(self._colours)
        self._position_animator = PositionAnimator(self)
        self._movement_duration = 0.5  # seconds
        self._movement_distance = 1 * 50  # units
        self._elapsed_time = 0
        self._is_moving = False
        self._directions = {UP: [0, -1],
                            DOWN: [0, 1],
                            LEFT: [-1, 0],
                            RIGHT: [1, 0]}
        self._moves = 0

    def handle_input(self, user_input):
        # TODO: stuff about states
        if self._is_moving is False:
            self._is_moving = True
        print('> input: {}, is_moving: {}'.format(user_input, self._is_moving))

    def move_up(self):
        # self._y -= self._speed
        self._facing = UP

    def move_down(self):
        # self._y += self._speed
        self._facing = DOWN

    def move_left(self):
        # self._x -= self._speed
        self._facing = LEFT

    def move_right(self):
        # self._x += self._speed
        self._facing = RIGHT

    @property
    def visual_representation(self):
        return self._colour_animator.current_colour

    def update(self, delta):
        self._colour_animator.animate(delta)
        # TODO: Move to PositionAnimator

        # print('> direction: ', self._directions[self._facing])

        if self._elapsed_time < self._movement_duration and self._is_moving:
            self._elapsed_time += delta

            positional_delta = self._movement_distance * (delta / self._movement_duration)
            print('> pos_delta: ', positional_delta)

            self._x += self._directions[self._facing][0] * positional_delta
            self._y += self._directions[self._facing][1] * positional_delta
            self._moves += 1
            print('> moves: {}, elapsed_t: {}, delta: {}'.format(self._moves, self._elapsed_time, delta))
        else:
            self._elapsed_time = 0
            self._is_moving = False
            self._moves = 0

