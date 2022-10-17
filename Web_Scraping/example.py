# BeautifulSoup을 활용하여 웹 스크레핑 연습!

from bs4 import BeautifulSoup
import lxml
# 데이터 불러와서 원하는 데이터 추출해보기
with open("website.html",encoding="UTF-8")as file:
    contents= file.read()

soup=BeautifulSoup(contents,"html.parser") # 오류 시 "html.parser" 대신하여 lxml로 가능


#===================================================
# soup.prettify() ==> 보기 좋게 HTML 내용확이 가능
#====================================================

# 모든 앵커태그를 가져오려면? find_all 활용
all_anchor_tags=soup.find_all(name='a')
# print(all_anchor_tags)

heading= soup.find(name="h3",id="name")
# print(heading)

section_heading=soup.find(name="h3",class_="heading")
print(section_heading.get('class'))