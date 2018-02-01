from entity import Entity
from sprite_animator import SpriteAnimator
import pygame
import os


class Critter(Entity):
    def __init__(self, vector):
        super().__init__(vector)
        self._sprite_animator = SpriteAnimator(self, self.load_png('link_02.png')[0])

    def load_png(self, name):
        """ Load image and return image object """
        fullname = os.path.join('data', name)
        try:
            image = pygame.image.load(fullname)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except pygame.error as e:
            print('Cannot load image:', fullname)
            raise SystemExit(e)
        return image, image.get_rect()

    def update(self, delta):
        self._sprite_animator.animate(delta)
        self._visual_representation = self._sprite_animator.current_sprite