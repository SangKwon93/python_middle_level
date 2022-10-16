# 구글 스프레드 시트를 이용하여 운동 추적 앱 만들기

import requests
from datetime import datetime
import os
from requests.auth import HTTPBasicAuth

# ////////////////////////////////////////////////////////////////////////////////////////
# 환경변수 해결
# File - settings - tools -terminal - Environment variables - 환경변수 추가하기
# 리눅스 명령어는 bash 환경에서 활용
# ////////////////////////////////////////////////////////////////////////////////////////





# 1단계 - API 인증 및 구글 스프레드 시트 준비하기
APP_ID=os.environ["APP_ID"]
APP_KEY=os.environ["APP_KEY"]
TOKEN = os.environ["TOKEN"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

# Basic Token 방식채택하여 인증
basic_headers = {
    "Authorization": f'Basic {TOKEN}'
}

exercise_input=input("무슨 운동을 하니?: ")

#==============================================================================================
# 떠올리지 못했던 코드 - 내 sheet url을 연결해줘야한다.
sheet_endpoint=os.environ["sheet_endpoint"]
#==============================================================================================

headers={
    "x-app-id":APP_ID,
    'x-app-key':APP_KEY,
}

param_excercise={
    "query":exercise_input,
    "gender":"male",
    "weight_kg":"62",
    "height_cm":"168",
    'age':'30'
}

# 2단계 - 자연어 쿼리로 운동 통계 얻기
service_endpoint='https://trackapi.nutritionix.com/v2/natural/exercise'

response= requests.post(url=service_endpoint,json=param_excercise,headers=headers )
result=response.json()
# print(result)

# 3단계 - sheety로 구글시트 준비하기

# https://sheety.co/ 로그인
# 프로젝트 페이지에서 새 프로젝트 클릭
# Sheety내에 새 프로젝트 Workout Tracking 생성
# ‘나의 운동’ 구글 시트의 URL 작성
# 운동 API 엔드포인트 클릭하고 get방식과 post방식 체크

# 4단계 - 구글 시트에 데이터 저장하기
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

#========================================================================================
# 떠올리지 못했던 코드
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


#========================================================================================

# 5단계 - Sheety API인증하기

# sheety 엔드포인트 보호하기 위해 Basic인증 토큰을 추가
# requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic) 예시 참고!
    sheet_response=requests.post(url=sheet_endpoint,json=sheet_inputs,headers=basic_headers)
    print(sheet_response.json())