import time
from turtle import Turtle, Screen
from paddles import Paddles
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
right_paddle = Paddles((350,0))
left_paddle = Paddles((-350,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect if ball hits top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect if ball hits the paddles
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 or ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    #Detect if the ball crossed Right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    #Detect if the ball crossed Left Paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()




    screen.onkey(right_paddle.move_up, "Up")
    screen.onkey(right_paddle.move_down, "Down")

    screen.onkey(left_paddle.move_up, "w")
    screen.onkey(left_paddle.move_down, "s")

screen.exitonclick()
