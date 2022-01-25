import pygame
import pymunk
import pygame_menu
from pygame_menu.examples import create_example_window
import pymunk.pygame_util
from typing import Tuple, Any, List


class BouncyBalls(object):
    from scenery import _add_static_scenery
    from run import run
    from events import _process_events
    from update import _update_balls
    from create import _create_ball
    from clear import _clear_screen
    from draw import _draw_objects

    def __init__(self, selection: int) -> None:
        # Space

        if selection == 1:
            self._space = pymunk.Space()
            self._space.gravity = (0.0, 978.0)
            print('1')
        elif selection == 2:
            self._space = pymunk.Space()
            self._space.gravity = (0.0, 125.0)
            print('2')

        # Physics
        # Time step
        self._dt = 1.0 / 60.0
        # Number of physics steps per screen frame
        self._physics_steps_per_frame = 1
        pygame.display.toggle_fullscreen()
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
        self._ticks_to_next_ball = 120


pygame.display.set_mode((pygame.display.Info().current_w,pygame.display.Info().current_h))
menu = pygame_menu.Menu(
    height=800,
    theme=pygame_menu.themes.THEME_ORANGE,
    title='Main Menu',
    width=600,

)

option = ['0']


def main_menu() -> None:
    menu.add.button('Play', play_simulation)    # TU JEST PROBLEM
    menu.add.selector('Place: ', [('Earth', 1), ('Moon', 2)], onchange=choice)
    menu.add.button('Quit', pygame_menu.events.EXIT)


def choice(value: Tuple[Any, int], number: str) -> None:
    option.clear()
    option.insert(0, number)


def play_simulation():

    if int(option[0]) == 1:
        App = BouncyBalls(option[0])
        App.run(1)
    elif int(option[0]) == 2:
        App = BouncyBalls(option[0])
        App.run(2)


surface = create_example_window('Simulation', (pygame.display.Info().current_w, pygame.display.Info().current_h))
main_menu()
menu.mainloop(surface)
    #App = BouncyBalls()             # TU JEST PROBLEM
    #App.run()
