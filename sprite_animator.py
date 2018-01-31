from animator import Animator
import pygame
from directions import *

IDLE_STATE = 'idle_state'
RUNNING_STATE = 'running_state'


class SpriteAnimator(Animator):
    def __init__(self, entity, sheet):
        super().__init__(entity)
        self._sheet = sheet
        self._strip = None
        self._strip_length = 9
        self._frame_size = 80
        self._colour_key = (0, 0, 0)  # black
        self._current_sprite = self.get_image(0, 0, self._frame_size, self._frame_size, self._sheet)
        self._state = IDLE_STATE
        self._animation_segments = 8
        self._animation_segment_length = 0.05  # seconds
        self._total_animation_duration = self._animation_segments * self._animation_segment_length
        self._elapsed_time = 0
        self._frame_index = 0

    def animate(self, delta):
        if delta < self._animation_segment_length and self._elapsed_time < self._animation_segment_length:
            self._elapsed_time += delta
        else:
            self._frame_index += 1
            self._elapsed_time = 0
            self._current_sprite = self.get_image(self._frame_index * self._frame_size,
                                                  0,
                                                  self._frame_size,
                                                  self._frame_size,
                                                  self._sheet)
            if self._frame_index >= self._animation_segments:
                self._frame_index = 0


    @property
    def current_sprite(self):
        return self._current_sprite

    # TODO: move to 'main.py'
    def scale_image(self, image, width, height):
        return pygame.transform.scale(image, (width, height))

    def get_strip(self, x_start, y_start, x_end, y_end):
        self._strip = self.get_image(x_start, y_start,
                                     (self._frame_size * self._strip_length),
                                     self._frame_size,
                                     self._sheet)

    def get_image(self, pos_x, pos_y, width, height, sprite_sheet):
        surface = pygame.Surface([width, height])
        surface.blit(sprite_sheet, (0, 0), (pos_x, pos_y, width, height))
        surface.set_colorkey(self._colour_key)
        return surface

    def set_direction(self, direction):
        if direction == UP:
            self.get_strip(0 * self._frame_size, 5 * self._frame_size,
                           6 * self._frame_size, self._frame_size)
        if direction == DOWN:
            self.get_strip(6 * self._frame_size, 5 * self._frame_size,
                           12 * self._frame_size, self._frame_size)
        if direction == LEFT:
            self.get_strip(6 * self._frame_size, 0 * self._frame_size,
                           9 * self._frame_size, self._frame_size)
        if direction == RIGHT:
            self.get_strip(0 * self._frame_size, 0 * self._frame_size,
                           9 * self._frame_size, self._frame_size)
