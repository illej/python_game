from animator import Animator
import pygame

IDLE_STATE = 'idle_state'
RUNNING_STATE = 'running_state'


class SpriteAnimator(Animator):
    def __init__(self, entity, sheet):
        super().__init__(entity)
        self._sheet = sheet
        self._strip = None
        self._strip_length = 9
        self._frame_size = 72
        self._colour_key = (0, 0, 0)  # black
        self._current_sprite = self.get_image(0, 0, self._frame_size, self._frame_size, self._sheet)
        self._state = IDLE_STATE
        self._animation_duration = 900  # milliseconds
        self._animation_frame_length = self._animation_duration / self._strip_length
        self._elpased = 0
        self._frame_index = 0

    def animate(self, delta):
        if self._elpased < self._animation_frame_length:
            self._elpased += delta
        else:
            self._current_sprite = self.get_image(self._frame_index * self._frame_size,
                                                  0,
                                                  self._frame_size,
                                                  self._frame_size,
                                                  self._sheet)
            self._frame_index += 1
            if self._frame_index == self._strip_length:
                self._frame_index = 0
            self._elpased = 0

    @property
    def current_sprite(self):
        return self._current_sprite

    # TODO: move to 'main.py'
    def scale_image(self, image, width, height):
        return pygame.transform.scale(image, (width, height))

    def get_strip(self, x_start, y_start, x_end, y_end):
        self._strip = self.get_image(0, 0,
                                     (self._frame_size * self._strip_length),
                                     self._frame_size,
                                     self._sheet)

    def get_image(self, pos_x, pos_y, width, height, sprite_sheet):
        image = pygame.Surface([width, height])
        image.blit(sprite_sheet, (0, 0), (pos_x, pos_y, width, height))
        image.set_colorkey(self._colour_key)
        return image