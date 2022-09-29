# 시행착오
# x= letter_text.replace("[name]","sk")
# print(x)

# f= open('/Users/psk/PycharmProjects/Mail Merge Project Start/Input/Letters/starting_letter.txt',mode='r')
# print(f.readline())
#     #
#     # letter_text=letter.read()
#     # # x= letter_text.replace("[name]","sk")
#     # print(letter_text)


#내 코드
PLACEHOLDER="[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names =name_file.readlines() # 강
    # print(names)


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_text=letter_file.read()
    # print(letter_text)
    for name in names:
        stripped_name=name.strip()
        # print(stripped_name)
        new_letter = letter_text.replace(PLACEHOLDER,stripped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)



