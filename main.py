# Zelda Souls
#
# Simple prototype for a 2D adventure game
#
# Released under the GNU General Public License

VERSION = '0.1'

try:
    import pygame
    import sys
    import os
    from time import time
    from pygame.locals import *
    from world import World
    from player import Player
    from critter import Critter
    from wall import Wall
except ImportError as e:
    print('Could not load module. {}'.format(e))
    sys.exit(2)

pygame.init()


def load_png(name):
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


DISPLAY_SURFACE = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('zelda_souls_v1')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

MAP = ["#####",
       "#c p#",
       "#   #",
       "#c  #",
       "#####"]

LEGEND = {'#': Wall,
          'p': Player,
          'c': Critter}

FPS = 30
fpsClock = pygame.time.Clock()
world = World(MAP, LEGEND)

def evaluate_entity(entity):
    result = None
    if type(entity) is Player:
        # return Player.visual_representation
        result = world.player.visual_representation
    elif type(entity) is Critter:
        # return RED
        result = RED
    elif type(entity) is Wall:
        # return BLACK
        result = BLACK
    elif entity is None:
        # return WHITE
        result = WHITE
    # print('> entity: {}, colour: {}'.format(entity, result))
    return result


def main():
    # world = World(MAP, LEGEND)
    print(world.to_string())

    print('player:', world.player)
    print('player_pos:', "{}, {}".format(world.player.x, world.player.y))

    entities = world.get_entities()
    print('entities:', entities)

    grid = world.get_grid()
    h = len(grid)
    w = len(grid[0])
    unit = 50

    # for y in range(h):
    #     for x in range(w):
    #         pygame.draw.rect(DISPLAY_SURFACE,
    #                          evaluate_entity(grid[y][x]),
    #                          (x * unit, y * unit, unit, unit))

    MOVE_KEYS = [K_UP, K_DOWN, K_LEFT, K_RIGHT]

    # frame time data
    frame_start_time = time()

    while True:
        DISPLAY_SURFACE.fill(WHITE)

        for i in range(len(entities)):
            e = entities[i]
            if e is not None:
                pygame.draw.rect(DISPLAY_SURFACE,
                                 evaluate_entity(e),
                                 (e.x, e.y, unit, unit))

        # DISPLAY_SURFACE.blit(catImg, (catx, caty))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # if event.key in MOVE_KEYS:
                #     world.player.handle_input(event.key)
                # TODO: Move to Player?
                world.player.handle_input(event.key)
                if event.key == K_UP:
                    world.player.move_up()
                if event.key == K_DOWN:
                    world.player.move_down()
                if event.key == K_LEFT:
                    world.player.move_left()
                if event.key == K_RIGHT:
                    world.player.move_right()

        frame_end_time = time()
        delta_time = frame_end_time - frame_start_time

        world.player.update(delta_time)

        frame_start_time = frame_end_time

        pygame.display.update()
        fpsClock.tick(FPS)

        # print('> f_start: {}'.format(frame_start_time))
        # print('> f_end: {}'.format(frame_end_time))
        # print('> delta: {}'.format(delta_time))






if __name__ == '__main__':
    main()