class TileMap(object):
    def __init__(self,
                 count_x, count_y,
                 upper_left_x, upper_left_y,
                 tile_width, tile_height,
                 tiles):
        self.count_x = count_x
        self.count_y = count_y
        self.upper_left_x = upper_left_x
        self.upper_left_y = upper_left_y
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tiles = tiles


class GameState(object):
    player_x = 0
    player_y = 0