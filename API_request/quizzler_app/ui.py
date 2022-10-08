THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz=quiz_brain

        super().__init__()
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.canvas=Canvas(width=300,height=250,bg="white")
        true_img=PhotoImage(file='images/true.png')
        false_img=PhotoImage(file='images/false.png')
        # 이미지 할당 시 self 없이 작성한다.
        # 버튼을 설정하는 것 외에는 사용하지 않기 때문에
        self.true_button =Button(image=true_img,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2,column=1)

        self.false_button= Button(image=false_img,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=0)

        self.question_text = self.canvas.create_text(150,125, width=280, text= "Who", fill=THEME_COLOR, font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        # tuple index out of range 오류 원인 : self.canvas.create_text(x,y)값을 넣어줘야한다.



        self.score_label=Label(text="score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
           
        else:
            self.canvas.itemconfig(self.question_text,text= "you've reached the end of the quiz")
            # 참과 거짓 불능화
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # def greeting(name:str) -> str:
    #     return 'Hello' + name

    def true_pressed(self):
        is_true = self.quiz.check_answer("True")
        self.give_feedback(is_true)

    def false_pressed(self):
        is_right= self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # mainloop()가 계속 진행되게 유지하기 때문에 time 대신 after를 활용
        self.window.after(1000,self.get_next_question)



