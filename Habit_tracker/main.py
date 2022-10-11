import requests
from datetime import datetime # data 새로 학습

# ======================================================================
# pixela 사용자 계정 설정 1단계
# Create your user account
# Call /v1/users API by HTTP POST.

USERNAME='psk'
TOKEN='sangkwonpark'

pixela_endpoint = "https://pixe.la/v1/users"

user_params={
    "token":TOKEN, # 패스워드
    "username":USERNAME, # 아이디
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
# 유저네임이나 토큰이 변경되면 1단계에서 생성하고 2단계로 넘어가야한다. -> 그렇지 않으면 오류가 발생한다.
# ======================================================================


# ======================================================================
# 2단계 그래프를 만드는 단계 - HTTP post가 아닌 새 엔드포인트로
# 헤더를 통해 인증하기
# Create a graph definition
# Call /v1/users/<username>/graphs by HTTP POST.
graph_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs'

# graph 파라미터
graph_config={
    "id":'bicycle',
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":'sora'
}

headers={
    "X-USER-TOKEN": TOKEN
}
# post 요청하기
response_graph =requests.post(url=graph_endpoint, json=graph_config,headers=headers)
print(response_graph.text)
# ======================================================================


# ======================================================================
# "User `skpark` does not exist or the token is wrong." -> 인증정보는 Request Header로
# 인증 방식 3가지
# 1. api key (권장)
# 2. X-api-key HTTP header -> api키가 로그나 요청 스니핑에서 타인에게 보이지 않게 하기 위함.
# 3. Authorization HTTP
# ======================================================================


# ======================================================================
# 3단계 - 픽셀 표시하기
# HTTP Method , API endpoint
# POST /v1/users/<username>/graphs/<graphID>
graph_id = graph_config['id']

today=datetime.now()
pixel_data ={
    "date":today.strftime("%Y%m%d"),
    "quantity": input("얼마나 자전거 탔니?")

}
graph_id_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs/{graph_id}'

response_graph_id= requests.post(url=graph_id_endpoint, json=pixel_data, headers=headers)
print(response_graph_id)
# ======================================================================


# ======================================================================
# 4단계 : 픽셀 업데이트 하기
# PUT /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

yyyymmdd = pixel_data["date"]
update_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{yyyymmdd}'

update_data ={
    "quantity":"9.8"
}

# response_update=requests.put(url=update_endpoint,json=update_data, headers=headers)
# print(response_update)
# ======================================================================


# ======================================================================
# 5단계 : 픽셀 제거하기
# DELETE /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
delete_endpoint =f'{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{yyyymmdd}'
# response_delete=requests.delete(url=delete_endpoint, headers=headers)
# print(response_delete.text)
# ======================================================================