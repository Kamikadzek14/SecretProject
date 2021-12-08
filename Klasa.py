import time
import pygame


class Color:
    # -----------------------------
    # FOR CONTRAST
    white = (255, 255, 255)
    black = (0, 0, 0)
    # -----------------------------
    # RGB COLORS
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    # -----------------------------
    # OTHER
    yellow = (255, 255, 0)
    light_blue = (0, 255, 255)


class Object:
    # PHYSICAL PROPERTIES
    mass = 0
    radius = 0
    width = radius
    distance = 0
    # GRAPHICAL PROPERTIES
    pos_x = 0
    pos_y = 0
    position = (pos_x, pos_y)
    chosen_color = Color.white


def show_object(display, color, x_y, radius, width):
    pygame.draw.circle(display, color, x_y, radius, width)


pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
# pygame.draw.circle(screen, (225, 225, 225), (50, 50), 15, 15)

# TESTOWANIE KLAS
object1 = Object()
object2 = Object()

object1.radius = 15
object2.radius = 30
object1.width = object1.radius
object2.width = object2.radius
object1.pos_x = 200
object1.pos_y = 100
object2.pos_x = 400
object2.pos_y = 400

object1.position = (object1.pos_x, object1.pos_y)
object2.position = (object2.pos_x, object2.pos_y)




# object1.chosen_color to Color.white (z definicji klasy)
object2.chosen_color = Color.light_blue

object3 = Object()
object3.pos_x = object1.pos_x
object3.chosen_color = Color.yellow
object3.radius = object1.radius
object3.width = object1.width
object3.position = (2.5*object3.pos_x, 2*object1.pos_y)
# WYŚWIETLENIE KLAS

show_object(screen, object1.chosen_color, object1.position, object1.radius, object1.width)
show_object(screen, object2.chosen_color, object2.position, object2.radius, object2.width)
show_object(screen, object3.chosen_color, object3.position, object3.radius, object3.width)
clock = pygame.time.Clock()
pygame.display.flip()
time.sleep(5)
