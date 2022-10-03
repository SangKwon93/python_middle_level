# 우리 집의 평수는 몇 평일까?

from tkinter import *
window=Tk()
window.title("평수를 알아보자")

window.config(padx=30,pady=30)


def sqft_unit():
    x_width=float(width_input.get())
    y_width = float(vertical_input.get())
    sqft=round((x_width*y_width)/3.3,3)
    result_init.config(text=f'{sqft}')

# 가로길이
width_input=Entry(width=7)
width_input.grid(column=1,row=0)

# 세로길이
vertical_input=Entry(width=7)
vertical_input.grid(column=2,row=0)

# 단위
unit_label=Label(text="㎡")
unit_label.grid(column=3,row=0)

# 미터 제곱 전환 멘트
comment=Label(text="변환 시")
comment.grid(column=0,row=1)

# 기초 값
result_init=Label(text="0")
# result_init.config(text="0")
result_init.place(x=90,y=20)

# 평 단위
sqft_label=Label(text="평")
sqft_label.grid(column=3,row=1)

# 계산 버튼
calculate_button = Button(text="계산하기",command=sqft_unit)
calculate_button.place(x=70,y=40)


window.mainloop()
