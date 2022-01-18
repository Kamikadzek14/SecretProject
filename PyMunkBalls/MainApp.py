

import sys
import pygame
import pymunk
import pygame_menu
from pygame_menu.examples import create_example_window

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
        self._space.gravity = (0.0, 978.0)

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
        self._ticks_to_next_ball = 60


pygame.display.set_mode((600,600))
menu = pygame_menu.Menu(
    height=600,
    theme=pygame_menu.themes.THEME_ORANGE,
    title='Main Menu',
    width=400
)
option = 2


def main_menu() -> None:
    menu.add.button('Play', choice(option))    # TU JEST PROBLEM
    menu.add.selector('Place: ', [('Earth', 1), ('Moon', 2)], onchange=choice(option))
    menu.add.button('Quit', pygame_menu.events.EXIT)


def choice(x):                      # TRZEBA
    x -= 1                          # NAPRAWIĆ
    if x == 1:                      # TĄ
        x += 1                      # FUNKCJĘ
        BouncyBalls().run()         # !


if __name__ == "__main__":
    surface = create_example_window('Simulation', (600, 600))
    main_menu()
    menu.mainloop(surface)
    App = BouncyBalls()             # TU JEST PROBLEM
    App.run()





