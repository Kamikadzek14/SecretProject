import turtle
from time import sleep
from Klasa import Object
import random


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Planets Collision")
wn.tracer(0)

#planet_Earth = Object(10,10,10,10)

planets = []

shapes = ["circle"]


Earth = planets.append(turtle.Turtle())
Moon = planets.append(turtle.Turtle())

for Earth in planets:
    Earth.shape(random.choice(shapes))
    Earth.shapesize(9, 9, 1)
    Earth.color("Blue")
    Earth.penup()
    Earth.speed(0)
    x = (-100)
    y = (0)
    Earth.goto(x, y)
    Earth.dy = 0
    Earth.dx = (1)
    Earth.da = (1)

for Moon in planets:
    Moon.shape(random.choice(shapes))
    Moon.shapesize(1, 1, 1)
    Moon.color("White")
    Moon.penup()
    Moon.speed(0)
    x = (200)
    y = (0)
    Moon.goto(x, y)
    Moon.dy = 0
    Moon.dx = (1)
    Moon.da = (1)

gravity = 0.1

while True:
    wn.update()
    sleep(0.01)

    for planet in planets:
        planet.rt(planet.da)
        planet.dy -= gravity
        planet.sety(planet.ycor() + planet.dy)
        planet.setx(planet.xcor() + planet.dx)

        # Wall collision
        if planet.xcor() > 700:
            planet.dx *= -1
            planet.da *= -1

        if planet.xcor() < -700:
            planet.dx *= -1
            planet.da *= -1
        # Bounce from floor
        if planet.ycor() < -400:
            planet.sety(-400)
            planet.dy *= 0.99
            planet.dy *= -1
            planet.da *= -1

    # Collision between planets
    for i in range(0, len(planets)):
        for j in range(i+1, len(planets)):
            # Check collision
            if planets[i].distance(planets[j]) < 20:
                temp_dx = planets[i].dx
                temp_dy = planets[i].dy

                planets[i].dx = planets[j].dx
                planets[j].dy = planets[j].dy

                planets[j].dx = temp_dx
                planets[j].dy = temp_dy

