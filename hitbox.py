class HitBox(object):
    def __init__(self, parent, x, y, w, h, is_active):
        self.parent = parent
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self._is_active = is_active

    def update(self, x, y):
        self.x = x
        self.y = y

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value):
        self._is_active = value
        if value is True:
            print('> {} ({}) @ {},{}, {}x{} (parent@{},{}'.format(
                self, self.is_active, self.x, self.y, self.width, self.height, self.parent.x, self.parent.y
            ))