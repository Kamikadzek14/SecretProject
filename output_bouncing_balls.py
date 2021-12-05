import sys
import os
import numpy
import matplotlib
import pygame






print("Secret_Project_X")

pygame.init()

size = width, height = 1400, 200
speed = [10, 0]
map(float, speed)
speed = [6, 0]
speed2 = [-5,0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)


ball1 = pygame.image.load(os.path.join('images', 'circle.png'))
ball2 = pygame.image.load(os.path.join('images', 'circle2.png'))
ball1rect = ball1.get_rect()
ball1rect.center = 32,100
ball2rect = ball2.get_rect()
ball2rect.center = 1300, 100
# w//2, h//2

clock = pygame.time.Clock()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

# Collision with walls
    ball1rect = ball1rect.move(speed)
    if ball1rect.left < 0 or ball1rect.right > width:
        speed[0] = -speed[0]
    if ball1rect.top < 0 or ball1rect.bottom > height:
        speed[1] = -speed[1]

    ball2rect = ball2rect.move(speed2)
    if ball2rect.left < 0 or ball2rect.right > width:
        speed2[0] = -speed2[0]
    if ball2rect.top < 0 or ball2rect.bottom > height:
        speed2[1] = -speed2[1]
    clock.tick(60)
# Collision with themselves



    collision_tollerance = 40
    if ball1rect.colliderect(ball2rect):
        if abs(ball2rect.top - ball1rect.bottom) < collision_tollerance:
            speed[1] = -speed[1]
        if abs(ball2rect.bottom - ball1rect.top) < collision_tollerance:
            speed[1] = -speed[1]
        if abs(ball2rect.right - ball1rect.left) < collision_tollerance:
            if speed[0] >= 0:
                speed[0] = -speed[0] - 1
            else: speed[0] = speed[0]+1
        if abs(ball2rect.left - ball1rect.right) < collision_tollerance:
            if speed[0] >= 0:
                speed[0] = -speed[0] + 1
            else: speed[0] = speed[0]-1

    if ball2rect.colliderect(ball1rect):
        if abs(ball1rect.top - ball2rect.bottom) < collision_tollerance:
            speed2[1] = -speed2[1]
        if abs(ball1rect.bottom - ball2rect.top) < collision_tollerance:
            speed2[1] = -speed2[1]
        if abs(ball1rect.right - ball2rect.left) < collision_tollerance:
            if speed2[0] > 0 :
                speed2[0] = -speed2[0] - 1
            else:    speed2[0] = speed2[0]+1
        if abs(ball1rect.left - ball2rect.right) < collision_tollerance:
            if speed2[0] >= 0:
                speed2[0] = -speed2[0] - 1
            else:    speed2[0] = speed2[0]+1



    screen.fill(black)
    screen.blit(ball1, ball1rect)
    screen.blit(ball2, ball2rect,)
    #screen.blit(ball2, ball2rect , to_pygame((450,100)))

    pygame.display.flip()










