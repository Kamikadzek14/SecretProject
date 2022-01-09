import sys
import os
import numpy as np
import matplotlib
import pygame
from time import sleep

window = height , width = (400,400)
screen = pygame.display.set_mode(window)


speed1 = [1,1]
speed2 = [2,1]

m1 = 10
m2 = 122



background = pygame.Surface(window)


Ball1 = pygame.draw.rect(background,(0,255,255),(20,20,40,40))
Ball2 = pygame.draw.rect(background,(255,0,255),(120,120,50,50))


screen.blit(background,(0,0))



pygame.display.flip()


clock = pygame.time.Clock()


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            clock.tick(60)
            sleep(0.001)

            # Collision with walls
            Ball1 = Ball1.move(speed1)
            if Ball1.left < 0 or Ball1.right > width:
                speed1[0] = -speed1[0]

            Ball2 = Ball2.move(speed2)
            if Ball2.left < 0 or Ball2.right > width:
                speed2[0] = -speed2[0]

            # Collision with themselves

            collision_tollerance = 400

            if Ball1.colliderect(Ball2):
                if abs(Ball2.left - Ball1.right) < collision_tollerance:
                    speed1[0] = ((speed1[0] * (m1 - m2) + 2 * m2 * speed2[0]) / (m1 + m2))

            if Ball2.colliderect(Ball1):
                if abs(Ball1.right - Ball2.left) < collision_tollerance:
                    speed2[0] = np.ceil((speed2[0] * (m2 - m1) + 2 * m1 * speed1[0]) / (m1 + m2))

            done = True
#### Update the the display and wait ####

pygame.quit()
