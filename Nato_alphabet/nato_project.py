#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas as pd
df =pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict={row.letter: row.code for (index,row) in df.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


# 내 코드
# answer = input("단어를 입력하시오\n")
# for letter in answer:
#     letter:code for (letter,code)in df.items()
#     # {new_key:new_value for (index,row) in df.iterrows()}


# 해답 코드
answer = input("단어를 입력하시오\n").upper()
output_lst = [nato_dict[letter] for letter in answer]
print(output_lst)