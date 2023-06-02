import requests # http 요청을 보내고 응답을 받는 데 사용하는 라이브러리(get, post, put, delete)
from bs4 import BeautifulSoup # html 및 xml 파일에서 데이터를 추출하는데 사용
from flask import Flask

# # 사용 방법
# url = "https://www.weather.go.kr/weather/observation/currentweather.jsp"
# html = requests.get(url).text
# soup = BeautifulSoup(html, "html.parser")
# print(soup)

app = Flask(__name__) # __name__은 현재 모듈의 이름
@app.route("/")

def get_weather():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

    # HTTP GET 요청
    response = requests.get(url)
    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    output = ""

    for loc in soup.select("location"):
        output += f"<h3>{loc.select_one('city').string}<h3>"
        output += f"날씨 : {loc.select_one('wf').string}</br>"
        output += f"최저/최고 기온 : {loc.select_one('tmn')}/{loc.select_one('tmx')}</hr>"
        
    return output