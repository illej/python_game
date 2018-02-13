from replay import Replay
from directions import Directions
from player_state import IdleState


class InputComponent(object):
    def __init__(self, controller):
        self._controller = controller
        self._replay = Replay()

    def update(self, actor):
        left_x, left_y = self._controller.get_left_stick()

        # TODO: Maybe let actor handle left stick state as well as buttons?
        if isinstance(actor._state, IdleState):
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
            elif abs_x < abs_y:
                if left_y > 0:
                    actor.set_direction(Directions.DOWN)
                else:
                    actor.set_direction(Directions.UP)
            else:
                actor.set_direction(None)

            # self._replay.left_stick_x.append(left_x)
            # self._replay.left_stick_y.append(left_y)

        buttons = self._controller.get_buttons()
        actor.handle_input(buttons)

        # self._replay.buttons.append(buttons)

    def show_replay_data(self):
        print('> left_x: ', self._replay.left_stick_x)
        print('> left_y: ', self._replay.left_stick_y)
        print('> buttons: ', self._replay.buttons)

