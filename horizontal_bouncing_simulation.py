import sys
import os
import numpy as np
import matplotlib
import pygame
from time import sleep


pygame.init()

size = width, height = 1400, 700

speed = [1, 0]
#list(np.float_(speed))   - will not work because the move function does not support float  :(
speed2 = [-1,0]

black = 0, 0, 0

screen = pygame.display.set_mode(size)


BigBall = pygame.draw.circle(screen, (0, 0, 0), (30, 30), 10 )
SmallBall = pygame.image.load(os.path.join('images', 'SmallBall.png'))
#BigBallrect = BigBall.get_rect()
#BigBallrect.center = 32,100
SmallBallrect = SmallBall.get_rect()
SmallBallrect.center = 1300, 100


# # Parameters of balls
# massBigBall =int(input("Insert mass of BigBall:"))
# massSmallBall =int(input("Insert mass of SmallBall:"))
#
#
# while massBigBall < massSmallBall:
#     print("massBigBall can not be smaller than massSmallBall\nTry Again")
#     massBigBall = int(input("Insert mass of BigBall:"))
#     massSmallBall = int(input("Insert mass of SmallBall:"))
#     if massBigBall > massSmallBall:
#         break

# m1 = massBigBall
# m2 = massSmallBall

m1 = 10000
m2 = 1000



clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    clock.tick(60)
    sleep(0.001)




    # Collision with walls
    BigBall = BigBall.move(speed)
    if BigBall.left < 0 or BigBall.right > width:
        speed[0] = -speed[0]

    SmallBallrect = SmallBallrect.move(speed2)
    if SmallBallrect.left < 0 or SmallBallrect.right > width:
        speed2[0] = -speed2[0]

    # Collision with themselves

    collision_tollerance = 400

    if BigBall.colliderect(SmallBallrect):
        if abs(SmallBallrect.left - BigBall.right) < collision_tollerance:
            speed[0] = ((speed[0] * (m1 - m2) + 2 * m2 * speed2[0]) / (m1 + m2))

    if SmallBallrect.colliderect(BigBall):
        if abs(BigBall.right - SmallBallrect.left) < collision_tollerance:
            speed2[0] = np.ceil((speed2[0] * (m2 - m1) + 2 * m1 * speed[0]) / (m1 + m2))



    screen.fill(black)
    screen.blit(BigBall, BigBall)
    screen.blit(SmallBall, SmallBallrect,)

    pygame.display.flip()