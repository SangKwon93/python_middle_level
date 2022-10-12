# 구글 스프레드 시트를 이용하여 운동 추적 앱 만들기

import requests
from datetime import datetime
import os
from requests.auth import HTTPBasicAuth

# ////////////////////////////////////////////////////////////////////////////////////////
# 환경변수 해결하지 못함
APP_ID='596157ab'
APP_KEY='de87979348b28c6a2dd5deba729ffee6'
USERNAME='skpark'
PASSWORD='sk138029'
sheet_endpoint='https://api.sheety.co/ff22574e21f64527aac328c9407e1105/workoutTracking/workouts'
TOKEN='c2twYXJrOnNrMTM4MDI5'
# ////////////////////////////////////////////////////////////////////////////////////////





# 1단계 - API 인증 및 구글 스프레드 시트 준비하기
APP_ID=os.environ["APP_ID"]
APP_KEY=os.environ["APP_KEY"]

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


# 3단계 - sheety로 구글시트 준비하기

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

    # sheet_response=requests.post(url=sheet_endpoint,json=sheet_inputs)
    #
    # print(sheet_response.text)


#========================================================================================

# 5단계 - Sheety API인증하기
# sheety 엔드포인트 보호하기 위해 Basic인증이나 Bearer 토큰을 추가
# requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic) 예시 참고!

    # USERNAME='skpark'
    # PASSWORD='sk138029'
    # Basic 인증
    sheet_response=requests.post(url=sheet_endpoint,json=sheet_inputs,auth=(os.environ["USERNAME"],os.environ["PASSWORD"]))

    # Bearer Token 인증
    bearer_headers = {
        "Authorization": f"Bearer {os.environ['TOKEN']}"
    }

    sheet_response=requests.post(url=sheet_endpoint,json=sheet_inputs,headers=bearer_headers)
    print(sheet_response)