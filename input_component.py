from replay import Replay


class InputComponent(object):
    # TODO: Possible to store stick and button state on each frame? In an array? [YES]
    # -> storage issue?
    # TODO: return input state to the player? Pass in 'entity' for callback? Use 'Command' pattern?
    def __init__(self, controller):
        self._controller = controller
        self._walk_acceleration = 1  # unused
        self._replay = Replay()

    def update(self, actor):
        left_x, left_y = self._controller.get_left_stick()

        actor.x += int(left_x * 5)
        actor.y += int(left_y * 5)

        # self._replay.left_stick_x.append(left_x)
        # self._replay.left_stick_y.append(left_y)

        buttons = self._controller.get_buttons()

        # self._replay.buttons.append(buttons)

    def show_replay_data(self):
        print('> left_x: ', self._replay.left_stick_x)
        print('> left_y: ', self._replay.left_stick_y)
        print('> buttons: ', self._replay.buttons)

