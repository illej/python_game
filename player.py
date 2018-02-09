from entity import Entity
import colours
from directions import Directions
from colour_animator import ColourAnimator
from position_animator import PositionAnimator
from sprite_animator import SpriteAnimator
import pygame
from pygame.locals import *
import os
from player_state import PlayerState, DuckingState, IdleState


class Player(Entity):
    def __init__(self, vector, input, physics, graphics):
        super().__init__(vector)
        self._input = input
        self._physics = physics
        self._graphics = graphics
        self._speed = 50
        self._velocity = 0  # ???
        self._direction = Directions.DOWN
        self._position_animator = PositionAnimator(self)
        self._movement_duration = 0.5  # seconds
        self._movement_distance = 1 * 50  # units
        self._elapsed_time = 0
        self._is_moving = False
        self._moves = 0
        self._sprite_animator = SpriteAnimator(self, self.load_png('dude_16_run_v3.png')[0])  # 'sun_bro_01.png')[0])
        self._image = None
        self._player_state = IdleState()

    def set_direction(self, direction):
        self._direction = direction
        self._sprite_animator.set_direction(direction)

    def set_graphic(self, animator):
        self._sprite_animator.set_animator(animator)

    def load_png(self, name):
        # TODO: Move out of this class?
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
        if self._is_moving is False:
            self._is_moving = True

        state = self._player_state.handle_input(self, user_input)
        if state:
            self._player_state = state
            self._player_state.enter(self)

    @property
    def image(self):
        self._image = self._sprite_animator.current_sprite
        return self._image

    def update(self, delta):
        # --- State Pattern --- #
        self._player_state.update(self)

        # --- Component Pattern --- #
        self._input.update(self)
        # self._physics.update(self)
        # self._graphics.update(self)

        self._sprite_animator.animate(delta)

        # Unused for now
        # self._position_animator.is_moving = self._is_moving
        # self._position_animator.animate(delta)
        # self._x += self._directions[self._facing][0] * self._position_animator.positional_delta
        # self._y += self._directions[self._facing][1] * self._position_animator.positional_delta

        self._image = self._sprite_animator.current_sprite

    def log_input(self):
        self._input.show_replay_data()

