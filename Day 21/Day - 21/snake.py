from  turtle import Turtle
from typing import Any

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Create a snake with three blocks
class Snake:
    snake = list[Any]

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        x = 0
        for _ in range(3):
            snake_segments = Turtle("square")
            snake_segments.color("white")
            snake_segments.penup()
            snake_segments.goto(x,0)
            x -= 20

            self.snake.append(snake_segments)

    def add_segment(self):
        new_snake_segment = Turtle("square")
        new_snake_segment.color("white")
        new_snake_segment.penup()
        new_snake_segment.goto(self.snake[-1].pos())
        self.snake.append(new_snake_segment)

    def move(self):
        for segments in range(len(self.snake) - 1 ,0,-1):
            self.snake[segments].goto(self.snake[segments-1].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
