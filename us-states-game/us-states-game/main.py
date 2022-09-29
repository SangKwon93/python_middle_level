import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state=


def get_mouse_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coor)

states = pd.read_csv("50_states.csv")
print(states)



turtle.mainloop()