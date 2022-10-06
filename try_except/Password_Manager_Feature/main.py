# 사이트별 패스워드 저장 json 형식으로 변경 + json형식 데이터로 관리 및 기록기능 추가

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# 비밀번호 만들기 프로젝트 코드 가져와서 형태에 맞게 변형
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# json형태 데이터 로딩하고 업데이트하고 저장하기
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data={
        website:{
        "email":email,
        "password": password,
        }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
            try:
                with open("data.json", "r") as data_file:
                    # 기존 데이터 로딩하기
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # 새로운 데이터 업데이트
                data.update(new_data)
                with open("data.json","w") as data_file:
                    # 업데이트된 데이터를 저장
                    json.dump(data,data_file,indent=4) # 데이터 json 파일에 넣기

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- find_password ------------------------------- #
# website만 가져와서 파일에 해당 데이터가 있는지 유무만 확인
# email = email_entry.get() 필요없음
# password = password_entry.get() 필요없음
def find_password():
    website = website_entry.get()
    # email = email_entry.get()
    # password = password_entry.get()

    try:
        with open("data.json", "r") as data_file:
            # 기존 데이터 로딩하기
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found")
    else:
        if website in data:
            email=data[website]["email"] # 특정 값(website)을 딕셔너리에서 뽑아서 key를 통해 해당 변수 할당
            password=data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email} \n Password:{password}.")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists ")

# ---------------------------- UI SETUP ------------------------------- #
# 창 만들기
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button=Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=2)

window.mainloop()