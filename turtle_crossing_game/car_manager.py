from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# 무작위로 차들 생성 + 스크린에서 움직임
# 색상/ 새로고침 할 때마다 차들 거리 정의

# 2. 화면에서 자동으로 자동차를 생성하고 움직임

####### 주석 내 코드 ######
###### 주석 밑에 올바른 코드 ######

class CarManager(Turtle):
    def __init__(self):
        self.all_car=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance == 1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            # new_car.setheading(180) -> 삭제 요망
            random_y=random.randint(-280,280)
            new_car.goto(300,random_y)
            # new_car.append(self.all_car)
            self.all_car.append(new_car)

    def move_cars(self):
        # self.backward(STARTING_MOVE_DISTANCE)
        for car in self.all_car:
            # car.forward(MOVE_INCREMENT)
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

