

import sys
import pygame
import pymunk


import pymunk.pygame_util
from pymunk.vec2d import Vec2d
from typing import List


from run import run
from scenery import _add_static_scenery


class BouncyBalls(object):
    from scenery import _add_static_scenery
    from run import run
    from events import _process_events
    from update import _update_balls
    from create import _create_ball
    from clear import _clear_screen
    from draw import _draw_objects


    def __init__(self) -> None:
        # Space
        self._space = pymunk.Space()
        self._space.gravity = (0.0, 900.0)

        # Physics
        # Time step
        self._dt = 1.0 / 60.0
        # Number of physics steps per screen frame
        self._physics_steps_per_frame = 1

        # pygame
        self._screen = pygame.display.set_mode((pygame.display.Info().current_w,pygame.display.Info().current_h))
        self._clock = pygame.time.Clock()

        self._draw_options = pymunk.pygame_util.DrawOptions(self._screen)

        # Static barrier walls (lines) that the balls bounce off of
        self._add_static_scenery()

        # Balls that exist in the world
        self._balls: List[pymunk.Circle] = []

        # Execution control and time until the next ball spawns
        self._running = True
        self._ticks_to_next_ball = 10


if __name__ == "__main__":
    App = BouncyBalls()
    App.run()





