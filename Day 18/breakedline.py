from turtle import Turtle, Screen

tim = Turtle()

for _ in range(10):
    tim.pendown()
    tim.forward(5)
    tim.penup()
    tim.forward(5)

Screen = Screen()
Screen.exitonclick()
