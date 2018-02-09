from replay import Replay
from directions import Directions


class InputComponent(object):
    # TODO: Possible to store stick and button state on each frame? In an array? [YES]
    # -> storage issue?
    # TODO: return input state to the player? Pass in 'entity' for callback? Use 'Command' pattern?
    def __init__(self, controller):
        self._controller = controller
        self._replay = Replay()

    def update(self, actor):
        left_x, left_y = self._controller.get_left_stick()

        actor.x += int(left_x * 5)
        actor.y += int(left_y * 5)

        abs_x = abs(left_x)
        abs_y = abs(left_y)
        abs_diff = abs(abs_x - abs_y)

        if abs_x > abs_y:
            if left_x > 0:
                actor.set_direction(Directions.RIGHT)
            else:
                actor.set_direction(Directions.LEFT)
        else:
            if left_y > 0:
                actor.set_direction(Directions.DOWN)
            else:
                actor.set_direction(Directions.UP)

        # self._replay.left_stick_x.append(left_x)
        # self._replay.left_stick_y.append(left_y)

        buttons = self._controller.get_buttons()

        # use state to evaluate individual button presses
        actor.handle_input(buttons)

        # self._replay.buttons.append(buttons)

    def show_replay_data(self):
        print('> left_x: ', self._replay.left_stick_x)
        print('> left_y: ', self._replay.left_stick_y)
        print('> buttons: ', self._replay.buttons)

