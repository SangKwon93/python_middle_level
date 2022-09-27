# 2. 우측 패들 만들기 - paddle
# 3. 좌측 패들 만들기 - paddle
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y=self.ycor() +20
        self.goto(self.xcor(),new_y)
        
    def go_down(self):
        new_y=self.ycor() - 20
        self.goto(self.xcor(),new_y)
