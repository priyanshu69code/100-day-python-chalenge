from turtle import Turtle, Screen
from rCgen import cgen

tim = Turtle()
colors = cgen()

tim.speed(0)
tim.pensize(2)


def semograph(a):
    for i in range(int(360/a)):
        tim.color(cgen.GenC())
        tim.circle(100)
        tim.setheading(tim.heading()+a)


semograph(5)
Screen = Screen()
Screen.exitonclick()
