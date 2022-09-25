import turtle
from turtle import Screen, Turtle
from snake import Snake

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()

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



is_game=True

while is_game:
    screen.update()
    time.sleep(0.1)
    snake.move()





screen.exitonclick()