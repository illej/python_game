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
    import xbox360_controller
    from hitbox import HitBox
except ImportError as e:
    print('Could not load module. {}'.format(e))
    sys.exit(2)

pygame.init()

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
WINDOW_HORIZONTAL_CENTRE = WINDOW_WIDTH / 2
WINDOW_VERTICAL_CENTRE = WINDOW_HEIGHT / 2

WINDOW_BACKGROUND_COLOUR = (255, 255, 255)  # (0, 0, 0)  # black

DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
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

grid = world.get_grid()
w = len(grid[0])
h = len(grid)
MAP_WIDTH = w * UNIT
MAP_HEIGHT = h * UNIT
MAP_HORIZONTAL_CENTRE = MAP_WIDTH / 2
MAP_VERTICAL_CENTRE = MAP_HEIGHT / 2


MAP_X_START = WINDOW_HORIZONTAL_CENTRE - MAP_HORIZONTAL_CENTRE
MAP_Y_START = WINDOW_VERTICAL_CENTRE - MAP_VERTICAL_CENTRE

TILE_WIDTH = UNIT_SIZE[0]
TILE_HEIGHT = UNIT_SIZE[1]


def truncate_float(f):
    return int(f)


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
    if isinstance(entity, Player):
        result = BLUE  # world.player.visual_representation
    elif isinstance(entity, Critter):
        result = RED
    elif isinstance(entity, Wall):
        result = BLUE
    elif isinstance(entity, HitBox):
        result = GREEN
    elif entity is None:
        result = WHITE
    return result


def draw_sprite(image):
    image_scaled = scale_image(image, UNIT_SIZE)
    DISPLAY_SURFACE.blit(image_scaled, (MAP_X_START + world.player.x, MAP_Y_START + world.player.y))


def draw_coloured_rect(entity):
    pygame.draw.rect(
        DISPLAY_SURFACE,
        evaluate_entity(entity),
        (MAP_X_START + entity.x, MAP_Y_START + entity.y, UNIT, UNIT)
    )


def draw_entities(entities):
    for entity in entities:
        if entity:
            draw_coloured_rect(entity)


def draw_hitboxes(entities):
    for entity in entities:
        if entity and entity._hitbox and entity._hitbox.is_active:
            draw_coloured_rect(entity._hitbox)


def main():
    # --- WEIRD SETUP THING --- #
    print(world.to_string())
    print('player:', world.player)
    print('player_pos:', "{}, {}".format(world.player.x, world.player.y))

    entities = world.get_entities()
    print('entities:', entities)

    # --- Draw player as sprite --- # TODO: Result sent to player/enemy constructor
    player_sheet, player_sheet_rect = load_png('sun_bro_01.png')
    enemy_sheet, enemy_sheet_rect = load_png('link_02.png')

    # frame time data
    frame_start_time = time()

    # --- Fixed time step, variable render  --- #
    _MS_PER_UPDATE = 0.01  # faster than 60fps (16ms~)
    _previous = time()
    _lag = 0.0

    while True:
        _current = time()
        _elapsed = _current - _previous
        _previous = _current
        _lag += _elapsed

        # handle_input()

        while _lag >= _MS_PER_UPDATE:
            # update()
            _lag -= _MS_PER_UPDATE

        # render()
        # ---------------------------- #

        # --- Handle input --- #
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # TODO: Move to Player?
                # TODO: Send input data to Player as Commands(stick_data)
                world.player.handle_input(event.key)
                if event.key == K_UP:
                    world.player.move_up()
                if event.key == K_DOWN:
                    world.player.move_down()
                if event.key == K_LEFT:
                    world.player.move_left()
                if event.key == K_RIGHT:
                    world.player.move_right()
            elif event.type == pygame.JOYBUTTONDOWN:
                # handle events for all controllers
                if event.button == xbox360_controller.START:
                    world.player.log_input()

        # --- UPDATE --- #
        world.update()

        new_player_x = world.player.x  # + value from xbox_controller
        new_player_y = world.player.y  # + value from xbox_controller

        player_tile_x = truncate_float((new_player_x - MAP_X_START) / TILE_WIDTH)
        player_tile_y = truncate_float((new_player_y - MAP_Y_START) / TILE_HEIGHT)

        is_valid = False

        if 0 <= player_tile_x < w and 0 <= player_tile_y < h:
            tile = grid[player_tile_y][player_tile_x]
            is_valid = tile is None

        if is_valid:
            world.player.x = new_player_x
            world.player.y = new_player_y

        print('> pl_tile_x,y:{},{}, wrld.pl.x,y:{},{}, MP_X,Y_ST:{},{}'.format(
            player_tile_x, player_tile_y,
            world.player.x, world.player.y,
            MAP_X_START, MAP_Y_START
        ))

        # --- RENDER --- #
        DISPLAY_SURFACE.fill(WINDOW_BACKGROUND_COLOUR)

        draw_entities(entities)
        draw_sprite(world.player.image)
        draw_hitboxes(entities)

        # --- End of frame --- #
        # TODO: Decide whether to use custom game loop or pygame loop
        frame_end_time = time()
        delta_time = frame_end_time - frame_start_time
        world.player.update(delta_time)  # -> UPDATE
        frame_start_time = frame_end_time

        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    main()