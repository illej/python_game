from entity import Entity
import colours
from directions import *
from colour_animator import ColourAnimator
from position_animator import PositionAnimator


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
        self._direction = UP
        self._colour_animator = ColourAnimator(self._colours)
        self._position_animator = PositionAnimator(self)

    def handle_input(self, user_input):
        # TODO: stuff about states
        pass

    def move(self):
        self._moves[self._direction]()

    def move_up(self):
        self._direction = UP
        self._y -= self._speed

    def move_down(self):
        self._direction = DOWN
        self._y += self._speed

    def move_left(self):
        self._direction = LEFT
        self._x -= self._speed

    def move_right(self):
        self._direction = RIGHT
        self._x += self._speed

    @property
    def visual_representation(self):
        return self._colour_animator.current_colour

    def update(self, delta):
        self._colour_animator.animate(delta)
        # self._position_animator.animate(delta) TODO: fix lol

    def positional_delta(self, delta):
        self._speed = delta
