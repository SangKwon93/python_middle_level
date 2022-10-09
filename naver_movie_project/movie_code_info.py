# 네이버 영화 디렉토리에서 영화코드 추출하기
import scrapy
import requests
from scrapy.http import TextResponse
from bs4 import BeautifulSoup
import os
import threading
from multiprocessing import Process

# 영화코드 얻기 함수 -> 마지막페이지 알아내고 처음부터 끝까지 링크주소 전처리하여 코드번호만 추출하기 
def get_MovieCode(gen):
    movieCode = []
    url = f"https://movie.naver.com/movie/sdb/browsing/bmovie.naver?genre={gen}&page=9999"
    # url="https://movie.naver.com/movie/sdb/browsing/bmovie.naver?genre=1"
    response = requests.get(url,timeout=3)
    txt = response.content
    soup = BeautifulSoup(txt, 'html.parser')

    #pagenavigation = soup.select('#old_content > div.pagenavigation')
    pagenavigation = soup.find('div', 'pagenavigation')
    # pagenavigation내 <a> 태그 중 마지막 태그의 text 값
    lastPage = pagenavigation.find_all('a')[-1].text.replace(',', '')

    for i in range(1, int(lastPage)+1):
        print(f"start page {i}")
        url = f'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?genre={gen}&page={i}'
        response2 = requests.get(url)
        txt = response2.content
        soup = BeautifulSoup(txt, 'html.parser')

        dir = soup.find('ul', 'directory_list')
        d_list = dir.findAll('a')
        
        for d in d_list:
            if '?code=' in str(d):
                # print(str(d).split('?code=')[1].split("")[0])
                movieCode.append(str(d).split('?code=')[1].split('"')[0])
    return movieCode

# 영화에 고유 장르번호 입력하여 영화코드 뽑아내기
if __name__ == '__main__':
    code_list = []
    for idx in range(2, 3):
        print(f"start gen {idx}")
        code_list += get_MovieCode(idx)
    print(code_list)

print(code_list)


















# import pandas as pd
# df=pd.DataFrame(code_list)
# df.to_csv('movie_list_data2(test).csv',index=False,header=False)

# fin_csv_list = [['영화제목', '평점', '감독']]

# for mo in code_list:
#     url=f'https://movie.naver.com/movie/bi/mi/detail.naver?code={mo}'
#     req3 = requests.get(url)
#     # txt = response3.content
#     response = TextResponse(req3.url, body=req3.text, encoding='utf-8')
#     title = response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]/text()').extract()[0]
#     # star = response.xpath('//*[@id="actualPointPersentBasic"]/div/span/span/text()').extract()[0][-5:-1]
#     director= response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a/text()').extract()[0]
    
#     fin_csv_list.append([title,director])

# df1=pd.DataFrame(code_list)
# df1.to_csv('test2.csv',index=True,header=True)
    

    
    