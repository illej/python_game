from abc import ABCMeta, abstractmethod
import xbox360_controller as xbox
from sprite_strip_animator import SpriteStripAnimator


class PlayerState(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def handle_input(self, actor, buttons):
        raise NotImplementedError

    @abstractmethod
    def update(self, actor):
        raise NotImplementedError

    @abstractmethod
    def enter(self, actor):
        raise NotImplementedError


class IdleState(PlayerState):
    def __init__(self):
        super().__init__()

    def handle_input(self, actor, buttons):
        for idx, button in enumerate(buttons):
            print('> button {} = {}'.format(idx, button))
        if buttons[5] == 1:  # right bumper
            return AttackState('light_attack')
        elif buttons[1] == 1:
            return DodgeState()
        return None

    def update(self, actor):
        pass

    def enter(self, actor):
        animator = SpriteStripAnimator('hyper_light_drifter.png', (0, 0, 32, 32), 1, 1, False, 10)
        actor.set_graphics(animator)


class MovingState(PlayerState):
    def __init__(self):
        super().__init__()

    def enter(self, actor):
        animator = SpriteStripAnimator('hyper_light_drifter.png', (0, 0, 32, 32), 12, 1, True, 10)
        actor.set_graphics(animator)

    def handle_input(self, actor, buttons):
        pass

    def update(self, actor):
        pass


class AttackState(PlayerState):
    def __init__(self, previous_state):
        super().__init__()
        self._previous_state = previous_state
        self._action_duration = 10  # frames
        self._elapsed_time = 0

    def enter(self, actor):
        actor.set_graphics('attack_sprite.png')

    def handle_input(self, actor, buttons):
        if self._previous_state == DodgeState:
            # idk, do something?
            actor.attack('rolling_attack')

    def update(self, actor):
        self._elapsed_time += 1
        if self._elapsed_time > self._action_duration:
            pass


class DodgeState(PlayerState):
    def __init__(self):
        super().__init__()
        self._action_duration = 0
        self._elapsed_time = 0

    def enter(self, actor):
        actor.set_graphics()
        actor.set_hitbox('inactive')

    def handle_input(self, actor, buttons):
        if buttons[5] == 1:
            return AttackState('rolling_attack')

    def update(self, actor):
        self._elapsed_time += 1
        if self._elapsed_time > self._action_duration:
            actor.set_hitbox('active')
            self._elapsed_time = 0
