from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)
        # self 키워드를 사용하여 터틀의 메소드와 속성을 사용한다.

    # 매소드의 첫 번째 매개변수는 항상 self 다
    def go_up(self):
        new_y=self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



# paddle= Turtle()
# paddle.shape("square")
# paddle.color("White")
# paddle.penup()
# paddle.shapesize(stretch_wid=5,stretch_len=1)
#
#
# position_x = 350
# position_y = 0
# paddle.goto(position_x, position_y)
#
# def go_up():
#     new_y=paddle.ycor() + 20
#     paddle.goto(paddle.xcor(),new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)
#
#
# screen.tracer(0)
#
# screen.onkey(go_up,"Up")
# screen.onkey(go_down,"Down")
#
# game_on = True
# while game_on:
#     screen.update()
#
#
# screen.exitonclick()
