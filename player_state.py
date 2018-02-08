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


class IdleState(PlayerState):
    def __init__(self):
        super().__init__()

    def handle_input(self, actor, input):
        if input == 'pressed_b':
            actor._player_state = JumpingState()

    def update(self, actor):
        pass


class DuckingState(PlayerState):
    def __init__(self):
        super().__init__()
        self._charge_time = 0
        self._max_charge = 10

    def handle_input(self, actor, input):
        if input == 'release_down':
            actor.change_sprite('img_stand')

    def update(self, actor):
        self._charge_time += 1
        if self._charge_time > self._max_charge:
            actor.super_bomb()


class JumpingState(PlayerState):
    def __init__(self):
        super().__init__()

    def handle_input(self, actor, input):
        pass

    def update(self, actor):
        pass
