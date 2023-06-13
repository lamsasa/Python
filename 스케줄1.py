import schedule # 스케줄링은 
import time
import requests
from bs4 import BeautifulSoup

def perform_web_crawling():
    # 웹 크롤링 작업 수행
    url = "http://www.naver.com"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

def job():
    print("웹 크롤링을 수행 합니다.")
    perform_web_crawling()

# 매일 정해진 시간에 동작하도록 구현
schedule.every().day.at("18:20").do(job)

# 1분에 한번씩 크롤링
# schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)