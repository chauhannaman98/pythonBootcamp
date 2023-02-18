from turtle import Turtle, Screen
from random import randint

tim = Turtle()

screen = Screen()
screen.colormode(255)

for i in range(3, 8):
    for _ in range(i):
        r = randint(0, 256)
        g = randint(0, 256)
        b = randint(0, 256)
        tim.pencolor(r, g, b)
        tim.forward(25)
        tim.right(360 / i)

screen.exitonclick()
