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
    from entity import Entity
except ImportError as e:
    print('Could not load module. {}'.format(e))
    sys.exit(2)

pygame.init()





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
UNIT = 50
UNIT_SIZE = (UNIT, UNIT)

FPS = 30
fpsClock = pygame.time.Clock()
world = World(MAP, LEGEND)


def scale_image(image, size):
    return pygame.transform.scale(image, (size[0], size[1]))

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


def get_image(pos_x, pos_y, width, height, sprite_sheet):
    image = pygame.Surface([width, height])
    image.blit(sprite_sheet, (0, 0), (pos_x, pos_y, width, height))
    image.set_colorkey(WHITE)
    return image


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

    # Draw player as sprite
    player_sheet, player_sheet_rect = load_png('sun_bro_01.png')
    enemy_sheet, enemy_sheet_rect = load_png('link_02.png')

    # for y in range(h):
    #     for x in range(w):
    #         pygame.draw.rect(DISPLAY_SURFACE,
    #                          evaluate_entity(grid[y][x]),
    #                          (x * unit, y * unit, unit, unit))

    MOVE_KEYS = [K_UP, K_DOWN, K_LEFT, K_RIGHT]

    # frame time data
    frame_start_time = time()

    # ---------------------------- #
    _MS_PER_UPDATE = 0.01  # faster than 60fps (16ms~)
    _previous = time()
    _lag = 0.0

    while True:
        _current = time()
        _elapsed = _current - _previous
        _previous = _current
        _lag += _elapsed

        # print('SETUP()_previous: {}, _current: {}, _elapsed: {}, _lag: {}'.format(_previous,
        #                                                                    _current,
        #                                                                    _elapsed,
        #                                                                    _lag))

        # handle_input()

        while _lag >= _MS_PER_UPDATE:
            # update()
            _lag -= _MS_PER_UPDATE
            # print('UPDATE()_lag: {}, _MSpu: {}'.format(_lag, _MS_PER_UPDATE))

        # render()
        # print('RENDER()')
        # ---------------------------- #

        DISPLAY_SURFACE.fill(BLACK)

        # Draw player as sprite
        player_image = get_image(0, 0, 76, 76, player_sheet)
        enemy_image = get_image(0, 0, 76, 76, enemy_sheet)
        player = scale_image(world.player.visual_representation, UNIT_SIZE)
        DISPLAY_SURFACE.blit(player, (world.player.x, world.player.y))

        # draw enemies
        for e in entities:
            if isinstance(e, Critter):
                enemy = scale_image(enemy_image, UNIT_SIZE)
                DISPLAY_SURFACE.blit(enemy, (e.x, e.y))

        # draw ALL entities
        for e in entities:  # TODO: change 'entities = world.get_entities()' to 'world.entities'
            if isinstance(e, Entity):
                e_img = scale_image(e.visual_representation, UNIT_SIZE)
                DISPLAY_SURFACE.blit(e_img, (e.x, e.y))


        # Draws map as coloured squares
        # for i in range(len(entities)):
        #     e = entities[i]
        #     if e is not None:
        #         pygame.draw.rect(DISPLAY_SURFACE,
        #                          evaluate_entity(e),
        #                          (e.x, e.y, unit, unit))

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


if __name__ == '__main__':
    main()