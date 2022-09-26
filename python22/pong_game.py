from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# 스크린 설정하기
screen=Screen()
screen.bgcolor("Black")
screen.setup(width=800,height=600)
screen.title("Pong-game")
screen.listen()
screen.tracer(0) # 애니메이션 작동 금지

ball=Ball()
scoreboard=Scoreboard()
# 공 받을 패드 두개 생성
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
# unexpected argument -> Paddle 클래스는 초기화 때 입력 값이 없었다.
# 개선하려면 Paddle 클래스에 인자 값 설정해야한다. def __init__(self,**position**)


# 2인용 방향키
screen.onkey(r_paddle.go_up ,"Up")
screen.onkey(r_paddle.go_down,"Down")

# 1인용 방향키
screen.onkey(l_paddle.go_up ,"w")
screen.onkey(l_paddle.go_down,"s")

# 게임 진행
game_on = True
while game_on:
    time.sleep(ball.move_speed) # 속도를 빠르게 하고 싶다면 이게 포인트! 숫자가 적을수록 빨라진다.
    screen.update()
    ball.move()

    # 위 아래 벽 충돌 감지
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()
    # 패널 맞고 팅겨나가기
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()

    # 오른쪽 패들 놓침 감지
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    # 왼쪽 패들 놓침 감지
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()

