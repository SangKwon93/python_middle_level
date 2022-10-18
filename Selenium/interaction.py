from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 위키백과 메인에서 기사글 수 추출하기

URL='https://en.wikipedia.org/wiki/Main_Page'

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
driver.get(URL)

article_number = driver.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')

from selenium.webdriver.common.keys import Keys

# 쉬운 링크 추출
log_in=driver.find_element(By.PARTIAL_LINK_TEXT,"Log in")
log_in.click()

driver.close()
driver.quit() 

