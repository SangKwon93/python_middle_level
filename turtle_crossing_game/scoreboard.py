from turtle import Turtle
FONT = ("Courier", 24, "normal")

# Level -플레이 레벨~ 게임종료까지 장면 기록
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score=1
        self.goto(-250, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # self.write(self.score, align="left", font=FONT)
        self.write(f"Level: {self.score}",align="left", font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=FONT)







