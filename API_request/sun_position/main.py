import smtplib
import time
import requests
from datetime import datetime
# ISS 머리 위에 알리미 프로젝트
# 런던
MY_LAT = 51.507351
MY_LONG = -0.127758
FORMAT = 0

# ISS와 내 위치가 -5~+5도에 들어와 있는지 확인
def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # ISS와 내 위치가 -5~+5도에 들어와 있는지 확인
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5:
        return True

# 밤인지 확인
def is_night():
    parameters={
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted": FORMAT
    }

    response=requests.get("https://api.sunrise-sunset.org/json", params=parameters) # . 주의
    # response=requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted={FORMAT}") # . 주의
    response.raise_for_status()
    data=response.json()
    sunrise=data['results']['sunrise'].split("T")[1].split(':')[0]
    sunset=data['results']['sunset'].split("T")[1].split(':')[0]

    time_now=datetime.now().hour

    if time_now >=sunset or time_now <=sunrise:
        return True
    # 내가 필요한 조건이 있다면 함수를 만들어서 전체 내용을 들여쓰기 하고 원하는 조건 기입후 return True로 작성해주면 된다.

# 밤이거나 내 머리 위에 있을 떄 접근했다고 메일로 전송하기
MY_EMAIL='apfhda7@gmail.com'
MY_PASSWORD='1111'

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look up \n\n The ISS is above you in the sky"
        )


