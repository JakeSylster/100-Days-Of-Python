import random
import turtle
from turtle import  Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(500, 400)
screen.textinput("Make your bet","Which turtle will win the race? Enter a color: ")
tom = []
tim.shape("turtle")
colors = ["red","green","blue","yellow","black","purple"]
speeds = []
tim.color("white")

y=-150
for i in range(6):
    tom.append(tim.clone())
    picked_color = random.choice(colors)
    tom[i].color(picked_color)
    colors.remove(picked_color)

    tom[i].penup()
    tom[i].setpos(-200,y)
    y += 50
    print(tom[i].pos())

for i in range(6):
    while tom[i].xcor() != 100:
        for j in range(6):
            picked_speed = random.choice(speeds)
            #tom[i].speed(picked_speed)
            tom[j].forward(picked_speed)

screen.exitonclick()