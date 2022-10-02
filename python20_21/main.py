import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# 스크린 창 만들기
screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=ScoreBoard()


# 뱀 키바인딩을 활용하여 이동하기
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


import time



# 게임 작동하기
is_game=True

while is_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # 먹이 충돌 감지
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # 벽에 충돌 감지 후 게임 종료
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # is_game =False # While문을 벗어난다.
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()


    # 꼬리와 충돌 시 종료
    for shape in snake.snake_shape:
        if shape == snake.head:
            pass
        elif snake.head.distance(shape)< 10:
            # is_game=False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()



screen.exitonclick()