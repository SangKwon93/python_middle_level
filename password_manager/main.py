from tkinter import * # 실제 모든 클래스와 상수만 임포트
from tkinter import messagebox # 또다른 모듈이다. 클래쓰가 아니기에 이렇게 개별적으로 import해준다.
from random import choice,randint,shuffle
# import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# 5회차 - 비밀번호 만들기 코드 참고
import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # 컴프리헨션으로 리펙토링
    password_letters=[random.choice(letters) for char in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_symbols=[random.choice(symbols) for char in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_numbers=[random.choice(numbers) for char in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list=password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)

    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
    # ---------------------------- SAVE PASSWORD ------------------------------- #
    # 웹사이트, 이메일/이름, 비밀번호 입력 후 add 누르면 data 파일에 내역 저장하기
    # 동시에 웹사이트와 비밀번호 초기화

def save():
    website= website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    # 입력 확인
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="오류!!",message="값이 입력되지 않았습니다.")
    else:


        # 확인 팝업창
        is_ok = messagebox.askokcancel(title=website,message=f"이메일:{email} \n 비밀번호:{password} \n 위 정보가 맞나요?")

        if is_ok:
            with open("info_data.txt","a")as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)









# ---------------------------- UI SETUP ------------------------------- #
# 흰 화면 만들기
window=Tk()
window.title("비밀번호 저장소")
window.config(padx=50,pady=50)

# 라벨 만들기
canvas=Canvas(width=200,height=200)
mypass_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=mypass_img)
canvas.grid(column=1,row=0)

website_label=Label(text="웹사이트")
website_label.grid(column=0,row=1)

email_label=Label(text="이메일/이름")
email_label.grid(column=0,row=2)

password_label=Label(text="비밀번호")
password_label.grid(column=0,row=3)

# entry 만들기
website_entry=Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus() # 실행 시 커서 놓기

email_entry=Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"apfhda7@naver.com")

password_entry=Entry(width=21)
password_entry.grid(column=1,row=3)

# 버튼 만들기
generate_password_button=Button(text="패스워드 추천",command=generate_password)
generate_password_button.grid(column=2,row=3)
add_button=Button(text="추가",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)







window.mainloop()