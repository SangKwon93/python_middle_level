import turtle
import pandas as pd

# 설계
# 입력 값이 csv파일 데이터 안에 있는지?
# 있다면 올바른 대답인지?
# 주 이름 쓰기를 turtle로 생성

screen = turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state= screen.textinput(title="Guess the state", prompt="다른 미국 주도 알려줘")
data = pd.read_csv("50_states.csv")
# x_y =data.loc[:,['x','y']]

for i in data:
    x_position=data['x'][i]
    y_position=data['y'][i]
    if answer_state in data.state:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_position,y_position)
        data[data['state'] == answer_state].goto(x_position,y_position)
        # 50개 주 좌표 데이터에서 내가 알고있는 주를 입력하면 해당 x,y 좌표로 이동해야한다.
        # x,y 각각 변수로 저장하여 이동시키려고 하였으나 오류가 남
        # for문 작성할 필요없이 해당주에 대한 행 전체를 변수로 정하고 그 안에서 변수.x, 변수.y 로 하여 turtle을 goto 할 수 있었다.


def get_mouse_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coor)






turtle.mainloop()