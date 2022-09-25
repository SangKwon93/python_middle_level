import turtle
from turtle import Screen, Turtle
from snake import Snake

# 스크린 창 만들기
screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()

# 뱀 키바인딩을 활용하여 이동하기
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


import time
# 방법1
# tim=turtle.Turtle()
# tim.shape("square")
# tim.color("white")
# tim.shapesize(1,3)

snake_shape=[]
# 방법2
# starting_position=[(0,0),(-20,0),(-40,0)]
# for position in starting_position:
#     seq=Turtle("square")
#     seq.color('white')
#     seq.penup()
#     seq.goto(position)
#     snake_shape.append(seq)


# 게임 작동하기
is_game=True

while is_game:
    screen.update()
    time.sleep(0.1)
    snake.move()





screen.exitonclick()