from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 10
        self.y_move=10
        self.move_speed=0.1
    
    # 4. 공이 화면에서 계속 움직이기 완료 - ball
    def move(self):
        new_x=self.xcor() + self.x_move
        new_y=self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
    # 5. 공이 벽과 부딪혔는지 감지 완료 - ball
    def bounce_y(self):
        self.y_move *=-1
    
    def bounce_x(self):
        self.x_move*= -1
        self.move_speed *= 0.9
        
    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()