# 기존 모듈을 활용
# 색 추출 활용하기
import random
--------------------------------------------------
import colorgram
colors = colorgram.extract('image.jpg', 6)
first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)
print(colors[0].rgb)

colors = colorgram.extract('image.jpg', 30)
color_lst=[]
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color=(r,g,b)
    color_lst.append(new_color)
------------------------------------------------------
# 색 추출을 바탕으로 점 10*10 그리기

color_list=[(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19),
(133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158),
(105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
(107, 127, 153), (174, 94, 97), (176, 192, 209)]
from turtle import Turtle, Screen
import turtle
turtle.colormode(255)
tim=turtle.Turtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.penup()
tim.hideturtle()

number_of_dots=100
for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count % 10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen= turtle.screen()
screen.exitonclick()
----------------------------------------------------






