# BeatifulSoup을 활용하여 특정 사이트에 기사 제목,링크,추천수 크롤링 

from bs4 import BeautifulSoup
import requests

URL='https://news.ycombinator.com/'
response = requests.get(URL)
yc_web = response.text

soup = BeautifulSoup(yc_web,"html.parser")
#print(soup.title)



# 기사 제목 및 링크
articles= soup.find_all("span",class_="titleline")

article_texts=[]
article_links=[]
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link=article_tag.find('a').get('href')
    article_links.append(article_link)

# find_all - 리스트를 가져오면 리스트에서는 getText 호출할 수 없다.


# # 기사 추천수
article_upvotes=[int(score.getText().split()[0]) for score in soup.find_all(name='span',class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

# 웹크롤링 허용 여부 /robots.txt