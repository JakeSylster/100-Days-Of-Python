# import colorgram
#
# colors = colorgram.extract("hirst-spots.jpg", 10)
# rgb = []
#
# for i in range(10):
#     color = colors[i].rgb
#     red = color.r
#     green = color.g
#     blue = color.b
#
#     new_color = (red,green,blue)
#     rgb.append(new_color)
# print(rgb)
import random
import turtle as t
from turtle import Turtle

tim = t.Turtle()
color_list = [ (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49)]

t.colormode(255)

tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.goto(-300.0,-300.0)
y = -300.0

for i in range(10):
    for j in range(10):
        color = random.choice(color_list)
        tim.pendown()
        tim.dot(20,color)
        tim.penup()
        tim.forward(50)
    y += 50
    tim.goto(-300.0, y)

t.exitonclick()
