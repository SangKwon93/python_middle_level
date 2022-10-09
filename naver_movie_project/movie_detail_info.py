# 고유 영화코드번호를 활용하여 세부사항 추출하기
import scrapy
import requests
from scrapy.http import TextResponse
from bs4 import BeautifulSoup
import os
import threading
from multiprocessing import Process
import pandas as pd
import csv
import time
from csv import reader
import numpy as np
# CSV 파일 불러오기
with open('movie_list_data22.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    temp= list(csv_reader)

# numpy 배열로 변경하기
temp1= np.array(temp)
temp1= temp1.flatten()

# numpy 배열에서 list 형태로 변경하기.
code_list = temp1.tolist()
# print(code_list)

#
# total_list=[['영화제목','영화감독','상영시간','상영국가','영화별점','영화관람등급','영화개봉일']]
# total_list=[['movie_titles','movie_directors','movie_total_times','movie_countries','movie_scores','movie_grades','movie_release_dates','movie_actors']]
movie_titles = []
movie_directors = []
movie_total_times = []
movie_countries = []
movie_scores = []
movie_grades = []
movie_years=[]
movie_release_dates = []

movie_actors= []

# from fake_useragent import UserAgent
# UserAgent().chrome
# print(UserAgent().chrome)

# 크롤러 작업시 설정해두는게 좋다.
# headers = {"User-Agent" : UserAgent().chrome }

for mo in code_list:
    url=f'https://movie.naver.com/movie/bi/mi/detail.naver?code={mo}'
    print(f"start page {mo}")
    # headers = {"User-Agent" : UserAgent().chrome }
    req3 = requests.get(url,headers=headers)
    response = TextResponse(req3.url, body=req3.text, encoding='utf-8')
    page=req3.content
    soup=BeautifulSoup(page,'html.parser')
    # time.sleep(0.2)
    
    
    
# 영화 제목
    try:
        movie_title = response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]/text()').extract()[0]
        movie_titles.append(movie_title)
    except:
        movie_titles.append(0)
# 영화감독
    
    try:
        movie_director= response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a/text()').extract()[0]
        movie_directors.append(movie_director)
    except:
        movie_directors.append(0)
    
# 영화 러닝타임
    try:
        movie_total_time = response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[3]/text()').extract()[0][:-2]
        movie_total_times.append(movie_total_time)
    except:
        movie_total_times.append(0)   

# 영화 국가
  
    try:
        movie_country=response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[2]/a/text()').extract()
        # movie_countries.append(movie_country)
        movie_countries.append('/'.join(movie_country))
    except:
        movie_countries.append(0)    
# ###############################################################################
#     countries = []
#     #movie_actor = soup.select_one('#content').find_all('a',class_='k_name')
#     movie_country = soup.select_one('.made_people')
    
  
#     if movie_country != None:
#         movie_country = movie_country.find_all('a',class_='k_name')
        
#         for p in movie_country:
#             if '?code=' in str(p):
#                     # print(str(d).split('?code=')[1].split("")[0])
#                     actors.append(str(p).split('?code=')[-1].split('"')[-1].strip('>').strip('</a>'))
#                     #.split('"')[-1]      
#         movie_countries.append('/'.join(countries))
#     else:
#         movie_countries.append(0)
# #################################################################################

    ## 별점 실패
    ttt= response.xpath('//*[@id="pointNetizenPersentBasic"]/em[1]/text()').extract()+response.xpath('//*[@id="pointNetizenPersentBasic"]/em[2]/text()').extract()+response.xpath('//*[@id="pointNetizenPersentBasic"]/em[3]/text()').extract()+response.xpath('//*[@id="pointNetizenPersentBasic"]/em[4]/text()').extract()
    movie_score= ''.join(ttt)
    # print(movie_score)

# 별점 성공
    if len(movie_score) > 0:
        # ttt= response.xpath('//*[@id="pointNetizenPersentBasic"]/em[1]/text()').extract()+response.xpath('//*[@id="pointNetizenPersentBasic"]/em[2]/text()').extract()+response.xpath('//*[@id="pointNetizenPersentBasic"]/em[3]/text()').extract()+response.xpath('//*[@id="pointNetizenPersentBasic"]/em[4]/text()').extract()
        # movie_score= ''.join(ttt)
        movie_scores.append(movie_score)
    else:
        movie_scores.append(0)
# print(movie_scores)     
# 영화 관람가
    try:
        movie_grade=response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[4]/p/a/text()').extract()
        movie_grades.append(movie_grade)
    except:
        movie_grades.append(0)

# 영화 개봉연도
    try:
        movie_year = response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[4]/a/text()').extract()[0]
        movie_years.append(movie_year)
    except:
        movie_years.append(0)
    
# 영화 개봉일자  movie_release_date
    try:
        movie_release_date = response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[4]/a/text()').extract()[0]+response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[4]/a/text()').extract()[1]
        movie_release_dates.append(movie_release_date)
    except:
        movie_release_dates.append(0)

# 영화 배우
    actors = []
    #movie_actor = soup.select_one('#content').find_all('a',class_='k_name')
    movie_actor = soup.select_one('.made_people')
    
  
    if movie_actor != None:
        movie_actor = movie_actor.find_all('a',class_='k_name')
        
        for p in movie_actor:
            if '?code=' in str(p):
                    # print(str(d).split('?code=')[1].split("")[0])
                    actors.append(str(p).split('?code=')[-1].split('"')[-1].strip('>').strip('</a>'))
                    #.split('"')[-1]      
        movie_actors.append('/'.join(actors))
    else:
        movie_actors.append(0)
                
    
# # 영화 배우
#     try:
#         movie_actor = soup.find('ul','lst_people').find_all('a', class_ = 'k_name')
#         for p in movie_actor:       
#             movie_actor=print(p.text)
#         movie_actors.append(movie_actor)
        
#     except:
#         movie_actors.append(0)
        
        
        # for p in movie_actor:
        #     print(p.text)
        # print(movie_actor)
            
    
    
# movie_info_list = pd.DataFrame(zip(movie_titles,movie_directors,movie_actors,movie_total_times,movie_stars,movie_grades,movie_release_date_list,movie_countrys),
#                             columns=['영화제목','감독','배우','영화총시간','별점','영화등급','개봉일자','국가'])
# movie_info_list.to_csv("movie_cult.csv", index=False)   








movie_info_list = pd.DataFrame(zip(movie_titles,movie_directors,movie_total_times,movie_countries,movie_scores,movie_grades,movie_years,movie_release_dates,movie_actors)
            ,columns=['영화제목','영화감독','상영시간','상영국가','영화별점','관람등급','개봉연도','개봉일자','출연진'])
movie_info_list.to_csv("new.csv", index=False)  
#movie_info_list.to_csv("movie_info_data22.csv", index=False)  
