# Tkinter를 활용하여 효율적인 공부 시간 카운트 프로그램 구현
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    check_point.config(text="")
    global reps
    reps=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    global reps
    reps +=1
    work_sec= WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

   # 내 코드
   #  is_continue = True
   #  while is_continue:
   #      global reps
   #      reps +=1
   #      if reps % 2 == 1:
   #          count_down(work_sec)
   #      elif reps % 2==0:
   #          count_down(short_break_sec)
   #      elif reps % 8==0:
   #          count_down(long_break_sec)
   #      else:
   #          is_continue=False
    # GUI창이 뜨나 렉걸림 -> 코드 오류

    # 강사 코드
    if reps % 8 ==0:
        count_down(long_break_sec)
        title_label.config(text="긴 휴식", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="짧은 휴식", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="학습 시작", fg=GREEN)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# 예시를 응용한 적용
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count% 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"
#==> 파이썬의 동적 타이핑을 통해서 int형태에서 str형태로 변경할 수 있다.

    # 제목 레이블을 변경하려면? title_label.config(text="")
    # 캔버스 요소를 변경하려면?
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    # print(count)

    if count >0 :
        global timer
        timer= window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        session=math.floor(reps/2)
        for _ in rang(session):
            marks += "✓"
        check_point.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("효율적인 시간분배")
window.config(padx=100,pady=50,bg=YELLOW)
# ------------------------------------------------------------------------
# 예시
# def say_something(a,b,c):
#     print(a,b,c)
#     window.after(1000,say_something,a-1,b-1,c-1)
#
# say_something(1,2,3)
# 결과값
# 1 2 3
# 0 1 2
# -1 0 1
# -2 -1 0
# -3 -2 -1
# ----------------------------------------------------------------------



title_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(column=1,row=0)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
# image 키워드 인수 작성 안하게 되면 아래 오류 발생
# unknown option "pyimage1"
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

# 카운트
# count_down(5)

start_button = Button(text="start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_point=Label(fg=GREEN,bg=YELLOW )
check_point.grid(column=1,row=3)

window.mainloop()
