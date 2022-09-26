import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        # self.food=Turtle()
        # 먹이 객체를 속성으로 만든다. -> Food 클래스가 Turtle 클래스를 상속받게 코드변경
        # 1.상속 시 class 명 옆에 상속 받으려는 클래스 명을 기입(Super class)
        # 2. 기입 시 초기화(init)이 자동기입 되며 그 안에서 상위 클래스 호출해야한다. ( super().__init__() )
        super().__init__() # 상위 클래스를 호출하지 않으면 아래 오류 발생.
        # 오류 발생 : 'Food' object has no attribute 'screen'
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) # 기존 20*20이고 원하는 크기는 10*10
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


