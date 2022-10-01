
# 판다스 데이터 프레임 반복 형식
student_dict={
    "student":["Angela","James","Lily"],
    "score":[56,76,88]
}

# 딕셔너리 반복
for (key,value) in student_dict.items():
    print(value)
# 결과값
#['Angela', 'James', 'Lily']
#[56, 76, 88]


 import pandas
# 딕셔너리 데이터프레임 만들기
student_data_frame=pandas.DataFrame(student_dict)
print(student_data_frame)
# 결과값
#   student  score
# 0  Angela     56
# 1   James     76
# 2    Lily     88

# 데이터프레임 반복 실행
for (key,value) in student_data_frame.items():
    print(value)
# 결과값
# 0    Angela
# 1     James
# 2      Lily
# Name: student, dtype: object
# 0    56
# 1    76
# 2    88
# Name: score, dtype: int64

# 데이터프레임 각 행을 반복 실행
for (index,row) in student_data_frame.iterrows():
    print(index)
# 결과값
# 0
# 1
# 2

# 특정 값 찾기
for (index,row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

# 데이터프레임 반복 형식
# {new_key:new_value for (index,row) in df.iterrows()}