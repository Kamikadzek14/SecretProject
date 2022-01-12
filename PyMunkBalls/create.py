import pymunk
import random
import pygame

def _create_ball(self) -> None:

    ball_image = pygame.image.load("Graphic\golf_ball.png")

    c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    mass = 10
    radius = 40
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    x = random.randint(100, 1000)
    y = random.randint(50, 700)
    body.position = x,y
    shape = pymunk.Circle(body, radius, (0, 0))
    shape.color = c
    shape.elasticity = 0.6
    shape.friction = 0.9
    self._space.add(body, shape)
    self._balls.append(shape)
    

    #pygame.Surface.blit(, ball_image, x, y)