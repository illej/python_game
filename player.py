from entity import Entity
import colours
from directions import *
from colour_animator import ColourAnimator
from position_animator import PositionAnimator
from sprite_animator import SpriteAnimator
import pygame
from pygame.locals import *
import os


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
        self._sprite_animator = SpriteAnimator(self, self.load_png('sun_bro_01.png')[0])

    def load_png(self, name):
        """ Load image and return image object """
        fullname = os.path.join('data', name)
        try:
            image = pygame.image.load(fullname)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except pygame.error as e:
            print('Cannot load image:', fullname)
            raise SystemExit(e)
        return image, image.get_rect()

    def handle_input(self, user_input):
        # TODO: stuff about states
        if self._is_moving is False:
            self._is_moving = True

    def move_up(self):
        # self._y -= self._speed
        self._facing = UP
        self._sprite_animator.set_direction(self._facing)

    def move_down(self):
        # self._y += self._speed
        self._facing = DOWN
        self._sprite_animator.set_direction(self._facing)

    def move_left(self):
        # self._x -= self._speed
        self._facing = LEFT
        self._sprite_animator.set_direction(self._facing)

    def move_right(self):
        # self._x += self._speed
        self._facing = RIGHT
        self._sprite_animator.set_direction(self._facing)

    @property
    def visual_representation(self):
        # return self._colour_animator.current_colour
        self._visual_representation = self._sprite_animator.current_sprite
        return self._visual_representation  # self._sprite_animator.current_sprite

    def update(self, delta):
        # self._colour_animator.animate(delta)
        self._sprite_animator.animate(delta)
        # TODO: Move to PositionAnimator
        # TODO: -> pass in [delta] and get back [positional_delta]
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
        self._visual_representation = self._sprite_animator.current_sprite

