from entity import Entity
import colours
from directions import Directions
from colour_animator import ColourAnimator
from position_animator import PositionAnimator
from sprite_animator import SpriteAnimator
import pygame
from pygame.locals import *
import os
from player_state import PlayerState, IdleState, AttackState
from sprite_strip_animator import SpriteStripAnimator
from hitbox import HitBox


class Player(Entity):
    def __init__(self, vector, input, physics, graphics):
        super().__init__(vector)
        self._input = input
        self._physics = physics
        self._graphics = graphics
        self._direction = Directions.DOWN
        self._position_animator = PositionAnimator(self)
        self._movement_duration = 0.5  # seconds
        self._movement_distance = 1 * 50  # units
        self._elapsed_time = 0
        self._is_moving = False
        self._attacking = False
        self._state = IdleState()
        self._idle_sprites = [
            SpriteStripAnimator('dude_16_run_v3.png', (0, 0, 16, 16), 4, 1, True, 10)
        ]
        self._move_sprites = [
            # file, rect, image_count, colour_key, is_looping, frame_duration
            # HLD
            SpriteStripAnimator('hyper_light_drifter.png', (0, 0, 32, 32), 12, 1, True, 2),
            SpriteStripAnimator('hyper_light_drifter.png', (0, 32, 32, 32), 12, 1, True, 2),
            SpriteStripAnimator('hyper_light_drifter.png', (0, 64, 32, 32), 12, 1, True, 2),
            SpriteStripAnimator('hyper_light_drifter.png', (0, 96, 32, 32), 12, 1, True, 2)
            # LINK
            # SpriteStripAnimator('link_no_cap_v04.png', (54, 0, 27, 32), 12, 1, True, 2),
            # SpriteStripAnimator('link_no_cap_v04.png', (0, 0, 27, 32), 14, 1, True, 2),
            # SpriteStripAnimator('link_no_cap_v04.png', (0, 0, 33, 32), 14, 1, True, 2),
            # SpriteStripAnimator('link_no_cap_v04.png', (0, 0, 33, 32), 14, 1, True, 2)
        ]
        self._attack_sprites = [
            SpriteStripAnimator('link_02.png', (0, 0, 80, 80), 10, 1, True, 10)
        ]
        self._attack_sprites_2 = {
            Directions.UP: SpriteStripAnimator('link_02.png', (0, 780, 120, 130), 10, 1, True, 2),
            Directions.DOWN: SpriteStripAnimator('link_02.png', (0, 520, 120, 130), 10, 1, True, 2),
            Directions.LEFT: SpriteStripAnimator('link_02.png', (0, 650, 120, 130), 10, 1, True, 2),
            Directions.RIGHT: SpriteStripAnimator('link_02.png', (0, 910, 120, 130), 10, 1, True, 2)
        }
        self._dodge_sprites = [
            SpriteStripAnimator('sun_bro_01.png', (0, 0, 80, 80), 9, 1, True, 10)
        ]
        self._sprite_animator = self._idle_sprites[0]
        self._image = self._sprite_animator.next()
        self._hitbox = HitBox(self, self.x, self.y, 100, 100, False)

    def update(self, delta):
        self._state.update(self)
        self._input.update(self)
        self._hitbox.update(self)
        self._image = self._sprite_animator.next()

    def handle_input(self, user_input):
        if self._is_moving is False:
            self._is_moving = True

        state = self._state.handle_input(self, user_input)
        if state:
            self._state = state
            self._state.enter(self)

    def set_direction(self, direction):
        """Sets the direction of the player

        Selects the associated sprite_animator

        :param direction: if direction is None, then select _idle_sprites[0]"""
        # TODO: Only set direction, move setting the _sprite_animator to .set_graphics()
        if direction:
            self._direction = direction

        if not isinstance(self._state, AttackState):
            if self._direction == Directions.UP:
                self._sprite_animator = self._move_sprites[0]
            elif self._direction == Directions.DOWN:
                self._sprite_animator = self._move_sprites[1]
            elif self._direction == Directions.LEFT:
                self._sprite_animator = self._move_sprites[2]
            elif self._direction == Directions.RIGHT:
                self._sprite_animator = self._move_sprites[3]
            else:
                self._sprite_animator = self._idle_sprites[0]

    def set_graphics(self, animator):
        if animator == 'attack':
            self._sprite_animator = self._attack_sprites_2[self._direction]

    @property
    def image(self):
        return self._image

    def attack(self, attack_type):
        if attack_type == 'light_attack':
            self._position_animator = PositionAnimator(self)
            self._position_animator.is_moving = True

            self._x += self._direction.value[0] * self._position_animator.positional_delta
            self._y += self._direction.value[1] * self._position_animator.positional_delta

    def log_input(self):
        self._input.show_replay_data()


