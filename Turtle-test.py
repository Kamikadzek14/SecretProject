import turtle
import random
from time import sleep

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Planets")
wn.tracer(0)


planets = []

for _ in range(20):
    planets.append(turtle.Turtle())

colors = ["red", "yellow", "green", "blue","white"]
shapes = ["circle"]

for planet in planets:
    planet.shape(random.choice(shapes))
    planet.color(random.choice(colors))
    planet.penup()
    planet.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(-100, 400)
    planet.goto(x, y)
    planet.dy = 0
    planet.dx = random.randint(-3, 3)
    planet.da = random.randint(-5, 5)


gravity = 0.1

while True:
    wn.update()
    sleep(0.015)

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
            if planets[i].distance(planets[j]) < 30:
                temp_dx = planets[i].dx
                temp_dy = planets[i].dy

                planets[i].dx = planets[j].dx
                planets[j].dy = planets[j].dy

                planets[j].dx = temp_dx
                planets[j].dy = temp_dy

