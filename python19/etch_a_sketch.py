from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def clock_right():
    new_heading=tim.heading()-10
    tim.setheading(new_heading)

def clock_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def reset():
    tim.reset()




screen.listen()

screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=clock_right)
screen.onkey(key="d",fun=clock_left)
screen.onkey(key="c",fun=reset)
screen.exitonclick()