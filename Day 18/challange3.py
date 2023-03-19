from turtle import Turtle, Screen
from rCgen import cgen

tim = Turtle()
colors = cgen()
for i in range(3, 11):
    tim.color(cgen.GenC())
    for _ in range(i):
        tim.forward(100)
        tim.right(360/i)

Screen = Screen()
Screen.exitonclick()
