import pygame
from pygame.locals import *
import sys
from tile_map import TileMap
from game_state import GameState

pygame.init()

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540
WINDOW_BACKGROUND_COLOUR = (0, 0, 0)

DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('zelda_souls_v2')


def main():
    GameState.player_x = 150
    GameState.player_y = 150

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                delta_player_x = 0
                delta_player_y = 0
                if event.key == K_UP:
                    delta_player_y = -1
                if event.key == K_DOWN:
                    delta_player_y = 1
                if event.key == K_LEFT:
                    delta_player_x = -1
                if event.key == K_RIGHT:
                    delta_player_x = 1
                GameState.player_x += delta_player_x * 60
                GameState.player_y += delta_player_y * 60

        tiles_00 = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        tiles_01 = [
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        tile_map_00 = TileMap(
            17, 9,
            -30, 0,
            60, 60,
            tiles_00
        )
        tile_map_01 = TileMap(
            17, 9,
            -30, 0,
            60, 60,
            tiles_01
        )

        upper_left_x = -30
        upper_left_y = 0
        tile_width = 60
        tile_height = 60

        DISPLAY_SURFACE.fill(WINDOW_BACKGROUND_COLOUR)

        for y in range(tile_map_00.count_y):
            for x in range(tile_map_00.count_x):
                tile = tile_map_00.tiles[y][x]
                grey = (125, 125, 125)
                if tile == 1:
                    grey = (255, 255, 255)
                min_x = upper_left_x + (x * tile_width)
                min_y = upper_left_y + (y * tile_height)
                max_x = tile_width
                max_y = tile_height
                pygame.draw.rect(DISPLAY_SURFACE, grey, (min_x, min_y, max_x, max_y))

        player_colour = (255, 255, 0)
        player_width = 0.75 * tile_width
        player_height = tile_height
        player_left = GameState.player_x - (0.5 * player_width)
        player_top = GameState.player_y - player_height
        pygame.draw.rect(DISPLAY_SURFACE,
                         player_colour,
                         (player_left, player_top,
                          player_width, player_height))

        pygame.display.update()


if __name__ == '__main__':
    main()
