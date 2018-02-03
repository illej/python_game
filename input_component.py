class InputComponent(object):
    def __init__(self, controller):
        self._controller = controller
        self._walk_acceleration = 1  # unused

    def update(self, actor):
        left_x, left_y = self._controller.get_left_stick()

        actor.x += int(left_x * 5)
        actor.y += int(left_y * 5)

        buttons = self._controller.get_buttons()

        # do stuff with buttons
