from abc import ABCMeta, abstractmethod


class PlayerState(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def handle_input(self, actor, input):
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

    def handle_input(self, actor, input):
        if input == 'press_b':
            return JumpingState()
        elif input == 'press_down':
            return DuckingState()
        return None

    def update(self, actor):
        pass

    def enter(self, actor):
        actor.set_graphics('idle_sprite.png')


class ActionState(PlayerState):
    def __init__(self):
        super().__init__()
        self._action_duration = 0
        self._elapsed_time = 0

    def enter(self, actor):
        actor.set_graphics('action_sprite.png')

    def handle_input(self, actor, input):
        pass

    def update(self, actor):
        pass


class DuckingState(PlayerState):
    def __init__(self):
        super().__init__()
        self._charge_time = 0
        self._max_charge = 10

    def handle_input(self, actor, input):
        if input == 'release_down':
            return IdleState()

    def update(self, actor):
        self._charge_time += 1
        if self._charge_time > self._max_charge:
            actor.super_bomb()


class JumpingState(PlayerState):
    def __init__(self):
        super().__init__()

    def handle_input(self, actor, input):
        if input == 'button_r1':
            return AttackState()

    def update(self, actor):
        pass


class AttackState(PlayerState):
    def __init__(self):
        super().__init__()

    def handle_input(self, actor, input):
        pass

    def update(self, actor):
        pass
