# One Call API에 API요청 하고 48시간 동안의 시간대별 예보

# 내코드
# import requests
# api_key='fc39cd559f368ab4a3dbd4a5977a6bc9'
# url="https://api.openweathermap.org/data/2.5/onecall"
# weather_params={
#     'lat':37.566536,
#     'lon':126.977966,
#     "appid": api_key
# }
# response=requests.get(url,params=weather_params)
# print(response.json())

# ==> API 요청하기 --> 원하고자하는 2.5/onecall 유료버전만 가능하게 변경되어 error 401이 계속뜸.

# 비가 오면 twilio 어플로 우산챙기라고 알려주기 연동 프로젝트
## ==> 데이터를 가지고 오지 못하여 코드 작성 위주로 학습
## ==> 직접 실습하지 못해 여러번 강의 반복함

# API로 데이터 접근해서 날씨번호코드만 추출하기
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "YOUR ACCOUNT SID"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": "YOUR LATITUDE",
    "lon": "YOUR LONGITUDE",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
# 날씨번호코드 700이하는 비가 온다.
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


# Twilio와 연동하여 비가 온다면 메세지 보내주기
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)

