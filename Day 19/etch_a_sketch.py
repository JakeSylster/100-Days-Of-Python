import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_anti_clockwise():
    tim.left(10)
def move_clockwise():
    tim.right(10)
def clear_and_restart():
    tim.reset()

screen.listen()
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_backward,key="s")
screen.onkey(fun=move_anti_clockwise,key="a")
screen.onkey(fun=move_clockwise,key="d")
screen.onkey(fun=clear_and_restart,key="c")

turtle.exitonclick()
