from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 크롬 옵션 세팅
def get_chrome_driver():
    # 1. 크롬 옵션 세팅
    chrome_options = webdriver.ChromeOptions()

    # 2. driver 생성하기
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),  # 가장 많이 바뀐 부분
        options=chrome_options
    )

    return driver

driver = get_chrome_driver()
driver.get('https://www.python.org/')

# update 내용 추출하기
title_lst= driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')

items=[]
for title in title_lst:
    item = title.text
    items.append(item)
#print(items)

# update 날짜 추출하기
time_lst = driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')

times=[]
for time in time_lst:
    date=time.text
    times.append(date)
#print(times)

# 내용과 날짜 zip으로 묶고 딕셔너리형태로 만들기
update_lst=dict(zip(times,items))
print(update_lst)

#===================================================================================================
#강사 코드
events={}
for n in range(len(times)):
    events[n]={
        "time":time_lst[n].text,
        'title':title_lst[n].text
    }
#===================================================================================================
# list를 활용하여 바로 딕셔너리 형태로 가공하기