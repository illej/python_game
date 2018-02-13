from sprite_sheet import SpriteSheet


class SpriteStripAnimator(object):
    """sprite strip animator

    This class provides an iterator (iter() and next() methods), and a
    __add__() method for joining strips which comes in handy when a
    strip wraps to the next row.
    """

    def __init__(self, filename, rect, count, colorkey=None, loop=False, frames=1):
        """construct a SpriteStripAnimator

        filename, rect, count, and colorkey are the same arguments used
        by sprite_sheet.load_strip.

        loop is a boolean that, when True, causes the next() method to
        loop. If False, the terminal case raises StopIteration.

        frames is the number of ticks to return the same image before
        the iterator advances to the next image.
        """
        self.filename = filename
        self.images = SpriteSheet(filename).load_strip(rect, count, colorkey)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames

    def iter(self):
        self.i = 0
        self.f = self.frames
        return self

    def next(self):
        # TODO: Replace 'self.frames' with 'delta' for variable image length.
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image

    def set_sprite_sheet(self, sprite_sheet):
        """Sets a new sprite sheet to be animated

        :param sprite_sheet: a SpriteSheet object
        :return:
        """
        self.images = sprite_sheet

    def __add__(self, sprite_sheet):
        self.images.extend(sprite_sheet.images)
        return self
