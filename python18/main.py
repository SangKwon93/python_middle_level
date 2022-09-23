import random
from turtle import Turtle, Screen

#속성 학습
timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
------------------------------------
#정사각형 그리기
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)

# 정사각형 그리기 - 반복문 활용
for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
------------------------------------
import turtle
tim=turtle.Turtle()
# 새 터틀 생성하기 -> 모듈이름.클래스이름()
------------------------------------
from turtle import *
# 장점 : * 모든 것을 임포트
# 단점 : 클래쓰 또는 메소드가 어디서 왔는지 파악 어려워
------------------------------------

# Q: 점선 그리기

for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

------------------------------------

# Q: turtle을 활용하여 삼각형에서 십각형 그리기

# 이중 for문을 활용한 방법(나)
lst=range(3,11)
for i in lst:
    for _ in range(0,i+1):
        tim.right(360/i)
        tim.forward(100)


# 함수를 활용한 방법(강사)
def draw_shape(num_sides):
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(360/num_sides)

for i in range(3,11):
    draw_shape(i)
------------------------------------

# Draw a Random Walk
import turtle as t

t.colormode(255)
# RGB tuple로 받아내기 (나의 코드)
def random_color():
    rgb_lst=[]
    r = random.randint(0, 255)
    rgb_lst.append(r)
    g = random.randint(0, 255)
    rgb_lst.append(g)
    b = random.randint(0, 255)
    rgb_lst.append(b)
    tuple_rgb= tuple(rgb_lst)
    return tuple_rgb

# RGB tuple로 받아내기 (강사 코드)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color= (r,g,b)
    return color

directions=[0,90,180,270]
tim.pensize(15)
tim.speed("fast")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading((random.choice(directions)))

------------------------------------

# 원겹쳐서 그리기

tim=t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color= (r,g,b)
    return color


tim.speed("fastest")

def draw_spriograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spriograph(5)

screen= Screen()
screen.exitonclick()