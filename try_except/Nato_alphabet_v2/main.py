# Nato 프로젝트 + 입력 값 예외처리 적용!

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. 딕셔너리 형태로 만들기
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)



#TODO 2. 알파벳이 아닌 숫자 기입 시 예외처리 적용
# 내 코드 - while문 활용
# ----------------------------------------------------------------------------------
# is_ok=True
# while is_ok:
#     try:
#         word = input("Enter a word: ").upper()
#         output_list = [phonetic_dict[letter] for letter in word]
#         print(output_list)
#         is_ok=False
#     except KeyError:
#             print("알파벳을 입력해주세요")
#             # word = input("Enter a word: ").upper()
# ----------------------------------------------------------------------------------

# 강사 코드 - 함수 활용
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("알파벳을 입력해주세요")
        generate_phonetic()
    # 제외의 경우에 위의 알파벳을 입력해주세요를 프린트하고 try로 다시 실행(반복)하려면 여기에 이 함수를 작성한다.
    else:
        print(output_list)

generate_phonetic()




