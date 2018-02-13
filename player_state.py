from abc import ABCMeta, abstractmethod
import xbox360_controller as xbox
from sprite_strip_animator import SpriteStripAnimator


class PlayerState(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def enter(self, actor):
        raise NotImplementedError

    @abstractmethod
    def handle_input(self, actor, buttons):
        raise NotImplementedError

    @abstractmethod
    def update(self, actor):
        raise NotImplementedError


class IdleState(PlayerState):
    def __init__(self):
        super().__init__()

    def enter(self, actor):
        print('> entering ', self)
        animator = SpriteStripAnimator('hyper_light_drifter.png', (0, 0, 32, 32), 1, 1, True, 10)
        actor.set_graphics(animator)
        # actor._hitbox.is_active = False  # TODO: this is in here temporarily

    def handle_input(self, actor, buttons):
        if buttons[5] == 1:
            return AttackState(self)
        elif buttons[1] == 1:
            return DodgeState()
        return None

    def update(self, actor):
        pass


class MovingState(PlayerState):
    def __init__(self):
        super().__init__()

    def enter(self, actor):
        print('> entering ', self)
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
        print('> entering ', self)
        actor.set_graphics('attack')
        actor._hitbox.is_active = True
        actor._hitbox.update(actor.x + actor._direction.value[0],
                             actor.y + actor._direction.value[1])

    def handle_input(self, actor, buttons):
        actor.attack('light_attack')
        if self._elapsed_time > self._action_duration:
            # return self._previous_state
            self.exit(actor)

    def update(self, actor):
        self._elapsed_time += 1

    def exit(self, actor):
        print('> finished attack.')
        actor._hitbox.is_active = False
        actor._state = self._previous_state


class DodgeState(PlayerState):
    def __init__(self):
        super().__init__()
        self._action_duration = 15
        self._elapsed_time = 0

    def enter(self, actor):
        print('> entering ', self)
        actor.set_graphics(SpriteStripAnimator('link_02.png', (0, 0, 32, 32), 10, 1, True, 10))
        # actor.set_hitbox('inactive')

    def handle_input(self, actor, buttons):
        new_state = IdleState()
        if buttons[5] == 1:
            new_state = AttackState(self)
        if self._elapsed_time > self._action_duration:
            return new_state

    def update(self, actor):
        self._elapsed_time += 1
        # if self._elapsed_time > self._action_duration:
        #     # actor.set_hitbox('active')
        #     self._elapsed_time = 0
