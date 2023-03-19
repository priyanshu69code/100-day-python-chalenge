from turtle import Turtle, Screen
from rCgen import cgen
from random import choice


def walk():
    tim = Turtle()
    tim.pensize(5)
    tim.speed("slowest")
    col = cgen()
    angles = [90, 180, 270]
    for _ in range(5000):
        tim.color(cgen.GenC())
        tim.forward(30)
        tim.right(choice(angles))


walk()


Screen = Screen()
Screen.exitonclick()
