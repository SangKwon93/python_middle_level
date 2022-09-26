import random
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"score board: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT , font=FONT)

    def increase_score(self):

        self.score +=1
        self.clear()
        self.update_scoreboard()




