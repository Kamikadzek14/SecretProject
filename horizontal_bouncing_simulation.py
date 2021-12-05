import sys
import os
import numpy
import matplotlib
import pygame

pygame.init()

size = width, height = 1400, 200
speed = [10, 0]
map(float, speed)
speed = [6, 0]
speed2 = [-5,0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)


BigBall = pygame.image.load(os.path.join('images', 'circle.png'))
SmallBall = pygame.image.load(os.path.join('images', 'circle2.png'))
BigBallrect = BigBall.get_rect()
BigBallrect.center = 32,100
SmallBallrect = SmallBall.get_rect()
SmallBallrect.center = 1300, 100


# Parameters of balls
massBigBall =input("Insert mass of BigBall:")
massSmallBall =input("Insert mass of SmallBall:")
while massBigBall < massSmallBall:
    print("massBigBall can not be smaller than massSmallBall\nTry Again")
    massBigBall = input("Insert mass of BigBall:")
    massSmallBall = input("Insert mass of SmallBall:")
    if massBigBall > massSmallBall:
        break




clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

# Collision with walls
    BigBallrect = BigBallrect.move(speed)
    if BigBallrect.left < 0 or BigBallrect.right > width:
        speed[0] = -speed[0]

    SmallBallrect = SmallBallrect.move(speed2)
    if SmallBallrect.left < 0 or SmallBallrect.right > width:
        speed2[0] = -speed2[0]

# Collision with themselves

collision_tollerance = 40

