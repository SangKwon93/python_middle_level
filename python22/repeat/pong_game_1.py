# 1.스크린 만들기
# 2. 우측 패들 만들기 - paddle
# 3. 좌측 패들 만들기 - paddle
# 4. 공이 화면에서 계속 움직이기 - ball
# 5. 공이 벽과 부딪혔는지 감지 - ball
# 6. 공을 다시 튕겨내고 패들에 부딪혔는지도 감지 - ball
# 7. 공을 놓치면 점수판 획득 - scoreboard
# 8. 점수판 기록 유지 - scoreboard

from turtle import Screen,Turtle
from paddle_1 import Paddle
from ball_1 import Ball
from scoreboard_1 import Scoreboard
import time
#1. 스크린 만들기
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong-Game")
screen.listen()
screen.tracer(0)


scoreboard=Scoreboard()

# 2~3번 완료
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()



# 2인용 방향키
screen.onkey(r_paddle.go_up ,"Up")
screen.onkey(r_paddle.go_down,"Down")

# 1인용 방향키
screen.onkey(l_paddle.go_up ,"w")
screen.onkey(l_paddle.go_down,"s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # 5. 공이 (아래)벽과 부딪혔는지 감지 - ball
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()
    # 6. 공을 다시 튕겨내고 패들에 부딪혔는지도 감지 - ball   
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()
    
    # 7. 공을 놓치면 점수판 획득 - scoreboard
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
        
    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        











screen.exitonclick()