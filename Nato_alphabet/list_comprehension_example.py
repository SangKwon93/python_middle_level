### 리스트 컴퓨리헨션
##### 제곱수 #####
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 내 코드
squared_numbers=[num*num for num in numbers]
# print(squared_numbers)

##### 짝수 필터링 #####
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 내 코드
result=[num for num in numbers if num % 2==0]
# print(result)

##### 겹치는 데이터 ##### hard

# 내 코드
result=[]
data_1=[]
data_2=[]
with open('file1.txt') as data1:
    data1 = data1.readlines()
    for data in data1:
        data=int(data.strip())
        data_1.append(data)
    #print(data_1)

with open('file2.txt') as data2:
    data2 = data2.readlines()
    for another in data2:
        another = int(another.strip())
        data_2.append(another)
    #print(data_2)

result=[i for i in data_1 if i in data_2]
print(result)


# 강사 코드
with open('file1.txt') as file1:
    file_1_data=file1.readlines()

with open('file2.txt') as file2:
    file_2_data=file2.readlines()

result=[int(num)for num in file_1_data if num in file_2_data]

print(result)

# 각 데이터들 뒤에 3\n 과 같이 공백이 붙었는데 이것은 문자열을 의미한다.
# strip()과 for문을 활용하여 공백을 제거하고 int 형태로 바꾸었다.
# => int 형태로 변환하면 문자열의 공백이 알아서 삭제된다.
# ==>굳이 for문을 통해 공백 제거할 필요없다.