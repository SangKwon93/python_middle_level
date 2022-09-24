from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()
----------------------------------------------------------------
ex) 예시
def move_forward():
    tim.forward(20)

screen.listen()
# 고차함수 - 다른 함수와 함께 작동하는 함수
# 함수를 인수로 사용할 때 ()를 제거해준다. 괄호를 그대로 넣어주면 함수가 작동한다.
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()
------------------------------------------------------------------
