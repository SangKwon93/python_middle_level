##### 딕셔너리 컴프리헨션#####
# 기본 형태 => new_dict = {new_key:new_value for (key,value) in dict.items() if test}
import random
names=['Alex','Beth','Dave','Max',"Jane"]
students_scores={student : random.randint(1,100) for student in names}

# 내 코드
passed_students= {name:score for student in students_scores if student.score >= 60}
print(passed_students)
==>'str' object has no attribute 'score' 해결 못함

# 강사 코드
passed_students_finished={student:score for (student,score) in students_scores.items() if score >=60}
print(passed_students_finished)

# 예제 1 - 문장에서 각각의 단어가 몇글자인지 딕셔너리로 만들기
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_lst =sentence.split()
# print(word_lst)
result= {word:len(word) for word in word_lst}
print(result)

# 딕셔너리 섭씨를 화씨로
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 기본 형태 => new_dict = {new_key:new_value for (key,value) in dict.items if test}



weather_f={day: tempeature*9/5+32 for (day,tempeature) in weather_c.items}
print(weather_f)

# Error- 'builtin_function_or_method' object is not iterable
# -> items에 ()를 넣지 않아서 생기는 오류
# --> item() 메소드 호출이기 때문에 괄호를 꼭 넣어야 오류가 안생긴다.


