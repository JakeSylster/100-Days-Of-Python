#Teachers solution
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="What turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
is_race_on = False
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won! {user_bet} won the race")
            else:
                print(f"You lost! {winning_color} won the race")
        random_distance = random.randint(1,10)
        turtle.forward(random_distance)

screen.exitonclick()
