# 설계
# 1.키로 거북이 움직임 제어
# 2. 화면에서 자동으로 자동차를 생성하고 움직임
# 3. 자동차와의 충돌 감지
# 4. 거북이 반대편으로 도달 탐지
# 5. 스코어보드를 만들어 우리가 있는 레벨 기록


import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
screen.listen()
carmanager=CarManager()
scoreboard=Scoreboard()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.clear()
    scoreboard.update_scoreboard()
    carmanager.create_car()
    carmanager.move_cars()


    # 충돌 감지 (새로 생성된 다수의 자동차와 거북이)
    for car in carmanager.all_car:
        if car.distance(player) <20:
            game_is_on=False
            scoreboard.game_over()

    # 성공적인 길 건너기
    if player.finish_success() :
        player.reset_position()
        carmanager.speed_up()
        scoreboard.increase_score()

screen.exitonclick()
