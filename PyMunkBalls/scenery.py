import pymunk
import pygame

pygame.init()

pygame.display.Info()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h


def _add_static_scenery(self) -> None:

    static_body = self._space.static_body
    static_lines = [
        pymunk.Segment(static_body, (0, 0), (0.0, height), 5.0),
        pymunk.Segment(static_body, (width, 0), (width, height), 5.0),
        pymunk.Segment(static_body, (0, height), (width, height), 10.0),
    ]

    for line in static_lines:
        line.elasticity = 0.95
        line.friction = 0.9
    self._space.add(*static_lines)
