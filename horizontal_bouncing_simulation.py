import sys
import os
import numpy as np
import matplotlib
import pygame

pygame.init()

size = width, height = 1400, 200

speed = [2, 0]
#list(np.float_(speed))   - will not work because the move function does not support float  :(
speed2 = [-2,0]

black = 0, 0, 0

screen = pygame.display.set_mode(size)


BigBall = pygame.image.load(os.path.join('images', 'BigBall.png'))
SmallBall = pygame.image.load(os.path.join('images', 'SmallBall.png'))
BigBallrect = BigBall.get_rect()
BigBallrect.center = 32,100
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

m1 = 1000
m2 = 1000



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

    collision_tollerance = 400

    if BigBallrect.colliderect(SmallBallrect):
        if abs(SmallBallrect.left - BigBallrect.right) < collision_tollerance:
            speed[0] = ((speed[0] * (m1 - m2) + 2 * m2 * speed2[0]) / (m1 + m2))

    if SmallBallrect.colliderect(BigBallrect):
        if abs(BigBallrect.right - SmallBallrect.left) < collision_tollerance:
            speed2[0] = np.ceil((speed2[0] * (m2 - m1) + 2 * m1 * speed[0]) / (m1 + m2))



    screen.fill(black)
    screen.blit(BigBall, BigBallrect)
    screen.blit(SmallBall, SmallBallrect,)

    pygame.display.flip()