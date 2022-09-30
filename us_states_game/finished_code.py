import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states) < 50:
    answer_state= screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()
    # title()은 모든 문자열에 사용가능하며 첫번쨰 문자는 대문자로 바꿔준다. 50개주 데이터 형식을 보면 앞글자만 대문자기 떄문에 맞춰준다.


    if answer_state == "Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        #t.write(state_data.state.item()) 데이터프레임의 열을 고르고 그 값을 찾는 방식






