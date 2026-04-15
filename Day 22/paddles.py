from turtle import Turtle

class Paddles(Turtle):

    def __init__(self,pos):
        super().__init__()

        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def move_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)





