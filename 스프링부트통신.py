import requests
import json

# JSON 데이터 생성
data = {
    "id" : "곰돌이사육사233",
    "pwd" : "sphb8250"
}

# JSON 데이터를 서버로 전달
url = "http://localhost:8111/login"
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

# 서버 응답 확인
if response.status_code == 200:
    print("데이터가 성공적으로 전송되었습니다.")
else:
    print("데이터 전송에 실패했습니다. 응답 코드:", response.status_code)