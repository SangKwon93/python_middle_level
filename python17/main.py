from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]

for question in question_data:
    question_text = question["text"]
    question_answer= question["answer"]
    new_question=Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was :{quiz.score}/{quiz.question_number} ")

## 객체 지향 프로그래밍을 통해 작성
# question_data 데이터의 양식이 달라져도
# question_text = ```question["text"]```
# question_answer= ```question["answer"]``` 이 부분만 수정하면 다른 용도로 활용도 가능하게 된다.