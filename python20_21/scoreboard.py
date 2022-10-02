import random
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


# 재시작을 하면 최고점수가 리셋되기에 data.txt를 만들어서 최고 점수를 계속 저장해서 추적하게 코드 리밸런싱

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open('data.txt') as data:
            self.high_score=int(data.read())

        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        # 최고점수도 표시
        self.write(f"Score board: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # game_over 메소드 제거
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT , font=FONT)

    # 리셋하고 최고점수 data.txt 기록하기
    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w")as data:
                data.write(f"{self.high_score}")
            self.score=0
            self.update_scoreboard()


    def increase_score(self):

        self.score +=1

        self.update_scoreboard()




