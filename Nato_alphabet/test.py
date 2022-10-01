# List Comprehension
name="samgkwon"
new_list=[letter for letter in name]
# print(new_list)

# 예제1
range_list=[num *2 for num in range(1,5)]
print(range_list)

# 글자가 5개 이상인 이름을 전부 대문자로 바꾸기
names=["Alex","Beth","Caroline","Dave","Elanor","Freddie"]

upper_long_letter=[name.upper() for name in names if len(name)>=5]
print(upper_long_letter)

#  변수 = [new_item for item in list if test]