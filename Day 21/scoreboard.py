from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier",25,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-10,y=270)
        self.color("white")
        self.hideturtle()

        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score = {self.score}", align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER.",align=ALIGNMENT,font=FONT
                             )
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
