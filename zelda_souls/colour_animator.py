import globals


class ColourAnimator(object):
    def __init__(self, colour_dict):
        self._colours = colour_dict
        self._state = list(colour_dict.keys())[0]  # 0
        self._animation_segments = len(self._colours)
        self._animation_segment_length = 1  # seconds TODO: will need to change if using variable length segments
        self._total_animation_length = self._animation_segments * self._animation_segment_length
        self._elapsed_time = 0
        self._fps_interval = 1000 / globals.FPS

    def _get_colour(self, state):
        return self._colours[state]

    def animate(self, delta):
        # TODO: flip the animation segment based on size of delta
        if delta < self._animation_segment_length and self._elapsed_time < self._animation_segment_length:
            self._elapsed_time += delta
        else:
            self._state += 1
            self._elapsed_time = 0
            if self._state > len(self._colours) - 1:
                self._state = 0

    @property
    def current_colour(self):
        return self._colours[self._state]
