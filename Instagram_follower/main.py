import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import os
chrome_driver_path="C:/Users/psk/chromedriver_win32" 
keyword='arsenal'

insta_id = os.environ["ID"]
insta_pw = os.environ['PW']


#함수를 만들기 위해 위와 같이 test
class InstaFollower():
    
    def __init__(self,path):
        # self.driver=webdriver.Chrome(executable_path=path)
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(20)
        id_input = self.driver.find_element(By.NAME,'username')
        id_input.click()
        id_input.send_keys(insta_id)
        time.sleep(1)
        password_input = self.driver.find_element(By.NAME,'password')
        password_input.click()
        password_input.send_keys(insta_pw)
        time.sleep(1)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)
    
    def find_followers(self):
        time.sleep(3)
        self.driver.get("https://www.instagram.com/Arsenal")
        time.sleep(2)
        # 팔로우 창 나오게 클릭
        # followers = self.driver.find_element(By.CSS_SELECTOR,".x78zum5.x1q0g3np.xieb3on a")
        followers=self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_Aa"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]')
        followers.click()
        time.sleep(2)
        
    def follow(self):
        # 팔로우 버튼에 해당하는 요소들 
        follower_button =self.driver.find_element(By.CLASS_NAME,'_acan._acap._acas')
        for person in follower_button:
            try:
                person.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button= self.driver.find_element(By.CLASS_NAME,'_a9--._a9_1')
                cancel_button.click()



bot=InstaFollower(chrome_driver_path)
bot.login()
time.sleep(5)
bot.find_followers()
time.sleep(5)
bot.follow()