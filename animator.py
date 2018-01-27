from abc import ABCMeta, abstractmethod


# TODO: accessor for 'current'
class Animator(metaclass=ABCMeta):
    def __init__(self, entity):
        self._entity = entity

    @abstractmethod
    def animate(self, delta):
        raise NotImplementedError
