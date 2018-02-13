from animator import Animator
import pygame
from directions import Directions
from sprite_strip_animator import SpriteStripAnimator

IDLE_STATE = 'idle_state'
RUNNING_STATE = 'running_state'


# TODO: Change this to be the client of the sprite_strip_animator. Change name to SpriteManager?
# It talks to the sprite_strip_animator, passing in the strip based on the player('entity') state.
# _current_sprite => strip[n].next().
# animate() has overlap with the .iter() method. Merge?#
# TODO: Design decision: decide whether a strip will have variable frame length per image, or duplicate images.
class SpriteAnimator(Animator):
    def __init__(self, entity, sheet):
        super().__init__(entity)
        self._sheet = sheet
        self._strip = None
        self._strip_length = 9
        self._frame_size = 16  # 80
        self._colour_key = (0, 0, 0)  # black
        self._current_sprite = None
        self._state = IDLE_STATE
        self._animation_segments = 4  # 8
        self._animation_segment_length = 0.15  # seconds
        self._variable_segment_lengths = {0: 0.05,
                                          1: 0.15,
                                          2: 0.05,
                                          3: 0.15}
        self._total_animation_duration = self._animation_segments * self._animation_segment_length
        self._elapsed_time = 0
        self._frame_index = 0
        # NEW
        self._frames = 2
        self._n = 1
        self._strip_animator = SpriteStripAnimator('hyper_light_drifter.png', (0, 0, 32, 32), 1, 1, True, 10)
        # moving
        self._strips = [
            SpriteStripAnimator('hyper_light_drifter.png', (0, 0, 32, 32), 12, 1, True, self._frames),
            SpriteStripAnimator('hyper_light_drifter.png', (0, 32, 32, 32), 12, 1, True, self._frames),
            SpriteStripAnimator('hyper_light_drifter.png', (0, 64, 32, 32), 12, 1, True, self._frames),
            SpriteStripAnimator('hyper_light_drifter.png', (0, 96, 32, 32), 12, 1, True, self._frames)
        ]
        self._strips[self._n].iter()
        self._idle_strips = [

        ]
        self._attack_strips = [
            SpriteStripAnimator('link_02.png', (0, 0, 32, 32), 10, 1, True, self._frames),
            SpriteStripAnimator('link_02.png', (0, 32, 32, 32), 10, 1, True, self._frames),
            SpriteStripAnimator('link_02.png', (0, 64, 32, 32), 10, 1, True, self._frames),
            SpriteStripAnimator('link_02.png', (0, 96, 32, 32), 10, 1, True, self._frames)
        ]

    def animate(self, delta):
        self._current_sprite = self._strip_animator.next()  # self._strips[self._n].next()

        # if delta < self._variable_segment_lengths[self._frame_index] and self._elapsed_time < self._variable_segment_lengths[self._frame_index]:
        #     self._elapsed_time += delta
        # else:
        #     self._frame_index += 1
        #     if self._frame_index >= self._animation_segments:
        #         self._frame_index = 0
        #     self._elapsed_time = 0
        #     self._current_sprite = self.get_image(self._frame_index * self._frame_size,
        #                                           0,
        #                                           self._frame_size,
        #                                           self._frame_size,
        #                                           self._sheet)

    @property
    def current_sprite(self):
        if self._current_sprite is None:
            self._current_sprite = self._strips[self._n].next()
        return self._current_sprite

    def set_direction(self, direction):
        # TODO: Temporary
        if direction == Directions.UP:
            self._n = 0
        if direction == Directions.DOWN:
            self._n = 1
        if direction == Directions.LEFT:
            self._n = 2
        if direction == Directions.RIGHT:
            self._n = 3

    def set_animator(self, animator):
        self._strip_animator = animator
        self._strip_animator.iter()
