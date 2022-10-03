# 여러 개의 인수를 취하는 함수
# *args(가변인수) - 몇 개 인수라도 허용 - 고정된 인수를 전달(n1=5,n2=3) - 튜플 형태 - 위치 기반
# **kwargs(가변 키워드인수) - 딕셔너리 형태 - 키워드 기반





from tkinter import *

window=Tk()
window.title("마일을 킬로미터로 바꾸자")
# 여백
window.config(padx=20,pady=20)

def miles_to_km():
    miles=float(miles_input.get())
    km=round(miles*1.609)
    kilometer_result_label.config(text=f"{km}")


miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

kilometer_result_label=Label(text="0")
kilometer_result_label.grid(column=1,row=1)

kilometer_label=Label(text="Km")
kilometer_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=1,row=2)
# text와 같은 인수 이름이 실수로 남겨져 있다면 오류 발생
# -> 'str' object has no attribute 'tk'





window.mainloop()