import sys
import os
import numpy as np
import matplotlib
import pygame

pygame.init()

size = width, height = 1400, 200

speed = [2, 0.0]
#list(np.float_(speed))   - will not work because the move function does not support float  :(
speed2 = [-1,0]

black = 0, 0, 0

screen = pygame.display.set_mode(size)


BigBall = pygame.image.load(os.path.join('images', 'BigBall.png'))
SmallBall = pygame.image.load(os.path.join('images', 'SmallBall.png'))
BigBallrect = BigBall.get_rect()
BigBallrect.center = 32,100
SmallBallrect = SmallBall.get_rect()
SmallBallrect.center = 1300, 100


# Parameters of balls
# massBigBall =input("Insert mass of BigBall:")
# massSmallBall =input("Insert mass of SmallBall:")
#
#
# while massBigBall < massSmallBall:
#     print("massBigBall can not be smaller than massSmallBall\nTry Again")
#     massBigBall = input("Insert mass of BigBall:")
#     massSmallBall = input("Insert mass of SmallBall:")
#     if massBigBall > massSmallBall:
#         break




clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    clock.tick(60)





    # Collision with walls
    BigBallrect = BigBallrect.move(speed)
    if BigBallrect.left < 0 or BigBallrect.right > width:
        speed[0] = -speed[0]

    SmallBallrect = SmallBallrect.move(speed2)
    if SmallBallrect.left < 0 or SmallBallrect.right > width:
        speed2[0] = -speed2[0]

    # Collision with themselves

    collision_tollerance = 30













    screen.fill(black)
    screen.blit(BigBall, BigBallrect)
    screen.blit(SmallBall, SmallBallrect,)

    pygame.display.flip()