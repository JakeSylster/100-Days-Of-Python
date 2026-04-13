import random
import turtle as t
from turtle import Turtle

tim = Turtle()

tim.shape("turtle")
tim.color("DarkGreen")
tim.penup()
tim.goto(-200,0)
tim.pendown()

#TODO 1.Make the turtle draw a square
def tim_drawing_a_square():
    for i in range(4):
        tim.forward(100)
        tim.left(90)

#TODO 2.Make the turtle draw a dashed line
def tim_drawing_a_dashed_line():
    for i in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

#TODO 3. Make the turtle draw polygons from 3 sided to 10 sided using a same edge
def tim_drawing_polygons():
    colors = ["aquamarine4", "blue4" , "chartreuse4" , "chocolate4" , "red" , "ForestGreen" ,"goldenrod1" , "gray0" , "purple" , "peru" ]
    sides = 3
    while sides <= 10:
        tim.color(random.choice(colors))
        for i in range(sides):
            tim.forward(50)
            tim.right(360/sides)
            tim.forward(50)
        sides += 1

#TODO 4. Make the turtle do a random walk with different colors
def tim_drawing_a_random_walk():
    colors = ["aquamarine4", "blue4", "chartreuse4", "chocolate4", "red", "ForestGreen", "goldenrod1", "gray0", "purple", "peru"]
    move = [0,90,180,270]
    tim.pensize(10)
    tim.speed("fastest")
    for i in range(100):
        tim.color(random.choice(colors))
        tim.setheading(random.choice(move))
        tim.forward(30)

#TODO 5. Make the turtle do a random walk with truly random colors
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r,g,b)
    return rand_color

def tim_drawing_a_truly_random_walk():
    move = [0, 90, 180, 270]
    t.colormode(255)
    tim.pensize(10)
    tim.speed("fast")

    for i in range(100):
        tim.color(random_color())
        tim.setheading(random.choice(move))
        tim.forward(30)

#TODO 6: Make the turtle draw a Spirograph
def tim_drawing_a_spirograph(size_of_gap):
    t.colormode(255)
    tim.pensize(1)
    tim.speed("fastest")
    for _ in range(int(360/size_of_gap)):
        tim.circle(100)
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)





tim_drawing_a_square()
tim_drawing_a_dashed_line()
tim_drawing_polygons()
#tim_drawing_a_random_walk()
tim_drawing_a_truly_random_walk()
tim_drawing_a_spirograph(5)

t.exitonclick()



