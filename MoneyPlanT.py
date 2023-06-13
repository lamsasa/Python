import os
import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pymysql



chrom_ver = chromedriver_autoinstaller.get_chrome_version()
print(chrom_ver)

chromedriver_autoinstaller.install(True)
chromedriver_path = f'./{chrom_ver.split(".")[0]}/chromedriver.exe'

print(chromedriver_path)
print(os.path.exists(chromedriver_path))
print(os.path.basename(chromedriver_path))

 # 반려동물
url = 'https://card-search.naver.com/list?benefitCategoryIds=10021&sortMethod=ri&isRefetch=true&bizType=CPC'
driver = webdriver.Chrome()
driver.get(url)


page_source = driver.page_source

card_imgs = []  # 이미지 링크를 저장할 배열
card_links = []  # 카드 링크를 저장할 배열

    # BeautifulSoup을 사용하여 페이지 소스를 파싱
soup = BeautifulSoup(page_source, 'html.parser')
names = soup.select("b.name")
descs = soup.select("p.desc")
annual_fees = soup.select("i.annual_fee")

links = soup.select("a.anchor")
for link_tag in links:
    card_link = link_tag.get("href")
    card_links.append(card_link)
        
imgs = soup.select("img.img")
for img_tag in imgs:
    card_img = img_tag.get("src")
    card_imgs.append(card_img)
    
    # 텍스트만 추출하여 출력
card_names = [element.text for element in names]
card_descs = [element.text for element in descs]
card_annual_fees = [element.text for element in annual_fees]

    # MySQL 데이터베이스에 연결
    # 메인 코드
conn = pymysql.connect(host="127.0.0.1", user="root", password="sbkm8531*", db="moneyplant", charset="utf8")
cursor = conn.cursor()
    
    # 크롤링한 결과를 MySQL에 저장
for name, desc, img, link, annual_fee in zip(card_names, card_descs, card_imgs, card_links, card_annual_fees):
        # SQL 쿼리 실행
    query = "INSERT INTO card_list (card_name, card_category, card_desc, card_img, card_link, card_annual_fee) VALUES (%s, %s, %s, %s,%s,%s)"
    values = (name,'반려동물', desc, img, 'https://card-search.naver.com'+link, annual_fee)
    cursor.execute(query, values)

    # 변경 사항 저장
conn.commit()

    # 연결 종료
conn.close()


driver.quit()



# 주유
url = 'https://card-search.naver.com/list?benefitCategoryIds=1&sortMethod=ri&isRefetch=true&bizType=CPC'
driver = webdriver.Chrome()
driver.get(url)
try:
    for _ in range(11):
        more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.more')))
        more_button.click()
        time.sleep(0.4)  # 1초 대기
        # 페이지의 모든 정보 가져오기
    page_source = driver.page_source

    card_imgs = []  # 이미지 링크를 저장할 배열
    card_links = []  # 카드 링크를 저장할 배열

    # BeautifulSoup을 사용하여 페이지 소스를 파싱
    soup = BeautifulSoup(page_source, 'html.parser')
    names = soup.select("b.name")
    descs = soup.select("p.desc")
    annual_fees = soup.select("i.annual_fee")

    links = soup.select("a.anchor")
    for link_tag in links:
        card_link = link_tag.get("href")
        card_links.append(card_link)
        
    imgs = soup.select("img.img")
    for img_tag in imgs:
        card_img = img_tag.get("src")
        card_imgs.append(card_img)
    
    # 텍스트만 추출하여 출력
    card_names = [element.text for element in names]
    card_descs = [element.text for element in descs]
    card_annual_fees = [element.text for element in annual_fees]

    # MySQL 데이터베이스에 연결
    # 메인 코드
    conn = pymysql.connect(host="127.0.0.1", user="root", password="sbkm8531*", db="moneyplant", charset="utf8")
    cursor = conn.cursor()
    
    # 크롤링한 결과를 MySQL에 저장
    for name, desc, img, link, annual_fee in zip(card_names, card_descs, card_imgs, card_links, card_annual_fees):
        # SQL 쿼리 실행
        query = "INSERT INTO card_list (card_name, card_category, card_desc, card_img, card_link, card_annual_fee) VALUES (%s, %s, %s, %s,%s,%s)"
        values = (name,'주유', desc, img, 'https://card-search.naver.com'+link, annual_fee)
        cursor.execute(query, values)

    # 변경 사항 저장
    conn.commit()

    # 연결 종료
    conn.close()

except TimeoutError:
    print('TimeOut')
finally:
    driver.quit()



# 식비
url = 'https://card-search.naver.com/list?benefitCategoryIds=14&sortMethod=ri&isRefetch=true&bizType=CPC'
driver = webdriver.Chrome()
driver.get(url)

try:
    for _ in range(11):
        more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.more')))
        more_button.click()
        time.sleep(0.4)  # 1초 대기
        # 페이지의 모든 정보 가져오기
    page_source = driver.page_source

    card_imgs = []  # 이미지 링크를 저장할 배열
    card_links = []  # 카드 링크를 저장할 배열

    # BeautifulSoup을 사용하여 페이지 소스를 파싱
    soup = BeautifulSoup(page_source, 'html.parser')
    names = soup.select("b.name")
    descs = soup.select("p.desc")
    annual_fees = soup.select("i.annual_fee")

    links = soup.select("a.anchor")
    for link_tag in links:
        card_link = link_tag.get("href")
        card_links.append(card_link)
        
    imgs = soup.select("img.img")
    for img_tag in imgs:
        card_img = img_tag.get("src")
        card_imgs.append(card_img)
    
    # 텍스트만 추출하여 출력
    card_names = [element.text for element in names]
    card_descs = [element.text for element in descs]
    card_annual_fees = [element.text for element in annual_fees]

    # MySQL 데이터베이스에 연결
    # 메인 코드
    conn = pymysql.connect(host="127.0.0.1", user="root", password="sbkm8531*", db="moneyplant", charset="utf8")
    cursor = conn.cursor()
    
    # 크롤링한 결과를 MySQL에 저장
    for name, desc, img, link, annual_fee in zip(card_names, card_descs, card_imgs, card_links, card_annual_fees):
        # SQL 쿼리 실행
        query = "INSERT INTO card_list (card_name, card_category, card_desc, card_img, card_link, card_annual_fee) VALUES (%s, %s, %s, %s,%s,%s)"
        values = (name,'식비', desc, img, 'https://card-search.naver.com'+link, annual_fee)
        cursor.execute(query, values)

    # 변경 사항 저장
    conn.commit()

    # 연결 종료
    conn.close()

except TimeoutError:
    print('TimeOut')
finally:
    driver.quit()




# 문화/레저
url = 'https://card-search.naver.com/list?benefitCategoryIds=18%2C19&sortMethod=ri&isRefetch=true&bizType=CPC'
driver = webdriver.Chrome()
driver.get(url)

try:
    for _ in range(4):
        more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.more')))
        more_button.click()
        time.sleep(0.4)  # 1초 대기
        # 페이지의 모든 정보 가져오기
    page_source = driver.page_source

    card_imgs = []  # 이미지 링크를 저장할 배열
    card_links = []  # 카드 링크를 저장할 배열

    # BeautifulSoup을 사용하여 페이지 소스를 파싱
    soup = BeautifulSoup(page_source, 'html.parser')
    names = soup.select("b.name")
    descs = soup.select("p.desc")
    annual_fees = soup.select("i.annual_fee")

    links = soup.select("a.anchor")
    for link_tag in links:
        card_link = link_tag.get("href")
        card_links.append(card_link)
        
    imgs = soup.select("img.img")
    for img_tag in imgs:
        card_img = img_tag.get("src")
        card_imgs.append(card_img)
    
    # 텍스트만 추출하여 출력
    card_names = [element.text for element in names]
    card_descs = [element.text for element in descs]
    card_annual_fees = [element.text for element in annual_fees]

    # MySQL 데이터베이스에 연결
    # 메인 코드
    conn = pymysql.connect(host="127.0.0.1", user="root", password="sbkm8531*", db="moneyplant", charset="utf8")
    cursor = conn.cursor()
    
    # 크롤링한 결과를 MySQL에 저장
    for name, desc, img, link, annual_fee in zip(card_names, card_descs, card_imgs, card_links, card_annual_fees):
        # SQL 쿼리 실행
        query = "INSERT INTO card_list (card_name, card_category, card_desc, card_img, card_link, card_annual_fee) VALUES (%s, %s, %s, %s,%s,%s)"
        values = (name,'문화/레저', desc, img, 'https://card-search.naver.com'+link, annual_fee)
        cursor.execute(query, values)

    # 변경 사항 저장
    conn.commit()

    # 연결 종료
    conn.close()

except TimeoutError:
    print('TimeOut')
finally:
    driver.quit()



# 마트/편의점
url = 'https://card-search.naver.com/list?benefitCategoryIds=16%2C7&sortMethod=ri&isRefetch=true&bizType=CPC'
driver = webdriver.Chrome()
driver.get(url)

try:
    for _ in range(5):
        more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.more')))
        more_button.click()
        time.sleep(0.4)  # 1초 대기
        # 페이지의 모든 정보 가져오기
    page_source = driver.page_source

    card_imgs = []  # 이미지 링크를 저장할 배열
    card_links = []  # 카드 링크를 저장할 배열

    # BeautifulSoup을 사용하여 페이지 소스를 파싱
    soup = BeautifulSoup(page_source, 'html.parser')
    names = soup.select("b.name")
    descs = soup.select("p.desc")
    annual_fees = soup.select("i.annual_fee")

    links = soup.select("a.anchor")
    for link_tag in links:
        card_link = link_tag.get("href")
        card_links.append(card_link)
        
    imgs = soup.select("img.img")
    for img_tag in imgs:
        card_img = img_tag.get("src")
        card_imgs.append(card_img)
    
    # 텍스트만 추출하여 출력
    card_names = [element.text for element in names]
    card_descs = [element.text for element in descs]
    card_annual_fees = [element.text for element in annual_fees]

    # MySQL 데이터베이스에 연결
    # 메인 코드
    conn = pymysql.connect(host="127.0.0.1", user="root", password="sbkm8531*", db="moneyplant", charset="utf8")
    cursor = conn.cursor()
    
    # 크롤링한 결과를 MySQL에 저장
    for name, desc, img, link, annual_fee in zip(card_names, card_descs, card_imgs, card_links, card_annual_fees):
        # SQL 쿼리 실행
        query = "INSERT INTO card_list (card_name, card_category, card_desc, card_img, card_link, card_annual_fee) VALUES (%s, %s, %s, %s,%s,%s)"
        values = (name,'마트/편의점', desc, img, 'https://card-search.naver.com'+link, annual_fee)
        cursor.execute(query, values)

    # 변경 사항 저장
    conn.commit()

    # 연결 종료
    conn.close()

except TimeoutError:
    print('TimeOut')
finally:
    driver.quit()



# 패션/미용
url = 'https://card-search.naver.com/list?benefitCategoryIds=20&sortMethod=ri&isRefetch=true&bizType=CPC'
driver = webdriver.Chrome()
driver.get(url)

try:
    for _ in range(4):
        more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.more')))
        more_button.click()
        time.sleep(0.4)  # 1초 대기
        # 페이지의 모든 정보 가져오기
    page_source = driver.page_source

    card_imgs = []  # 이미지 링크를 저장할 배열
    card_links = []  # 카드 링크를 저장할 배열

    # BeautifulSoup을 사용하여 페이지 소스를 파싱
    soup = BeautifulSoup(page_source, 'html.parser')
    names = soup.select("b.name")
    descs = soup.select("p.desc")
    annual_fees = soup.select("i.annual_fee")

    links = soup.select("a.anchor")
    for link_tag in links:
        card_link = link_tag.get("href")
        card_links.append(card_link)
        
    imgs = soup.select("img.img")
    for img_tag in imgs:
        card_img = img_tag.get("src")
        card_imgs.append(card_img)
    
    # 텍스트만 추출하여 출력
    card_names = [element.text for element in names]
    card_descs = [element.text for element in descs]
    card_annual_fees = [element.text for element in annual_fees]

    # MySQL 데이터베이스에 연결
    # 메인 코드
    conn = pymysql.connect(host="127.0.0.1", user="root", password="sbkm8531*", db="moneyplant", charset="utf8")
    cursor = conn.cursor()
    
    # 크롤링한 결과를 MySQL에 저장
    for name, desc, img, link, annual_fee in zip(card_names, card_descs, card_imgs, card_links, card_annual_fees):
        # SQL 쿼리 실행
        query = "INSERT INTO card_list (card_name, card_category, card_desc, card_img, card_link, card_annual_fee) VALUES (%s, %s, %s, %s,%s,%s)"
        values = (name,'패션/미용', desc, img, 'https://card-search.naver.com'+link, annual_fee)
        cursor.execute(query, values)

    # 변경 사항 저장
    conn.commit()

    # 연결 종료
    conn.close()

except TimeoutError:
    print('TimeOut')
finally:
    driver.quit()


# 여행/숙박
url = 'https://card-search.naver.com/list?benefitCategoryIds=19&subBenefitCategoryIds=47&sortMethod=ri&isRefetch=true&bizType=CPC'
driver = webdriver.Chrome()
driver.get(url)

try:
    for _ in range(1):
        more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.more')))
        more_button.click()
        time.sleep(0.4)  # 1초 대기
        # 페이지의 모든 정보 가져오기
    page_source = driver.page_source

    card_imgs = []  # 이미지 링크를 저장할 배열
    card_links = []  # 카드 링크를 저장할 배열

    # BeautifulSoup을 사용하여 페이지 소스를 파싱
    soup = BeautifulSoup(page_source, 'html.parser')
    names = soup.select("b.name")
    descs = soup.select("p.desc")
    annual_fees = soup.select("i.annual_fee")

    links = soup.select("a.anchor")
    for link_tag in links:
        card_link = link_tag.get("href")
        card_links.append(card_link)
        
    imgs = soup.select("img.img")
    for img_tag in imgs:
        card_img = img_tag.get("src")
        card_imgs.append(card_img)
    
    # 텍스트만 추출하여 출력
    card_names = [element.text for element in names]
    card_descs = [element.text for element in descs]
    card_annual_fees = [element.text for element in annual_fees]

    # MySQL 데이터베이스에 연결
    # 메인 코드
    conn = pymysql.connect(host="127.0.0.1", user="root", password="sbkm8531*", db="moneyplant", charset="utf8")
    cursor = conn.cursor()
    
    # 크롤링한 결과를 MySQL에 저장
    for name, desc, img, link, annual_fee in zip(card_names, card_descs, card_imgs, card_links, card_annual_fees):
        # SQL 쿼리 실행
        query = "INSERT INTO card_list (card_name, card_category, card_desc, card_img, card_link, card_annual_fee) VALUES (%s, %s, %s, %s,%s,%s)"
        values = (name,'여행/숙박', desc, img, 'https://card-search.naver.com'+link, annual_fee)
        cursor.execute(query, values)

    # 변경 사항 저장
    conn.commit()

    # 연결 종료
    conn.close()

except TimeoutError:
    print('TimeOut')
finally:
    driver.quit()



# 주거
url = 'https://card-search.naver.com/list?benefitCategoryIds=8%2C10&sortMethod=ri&isRefetch=true&bizType=CPC'
driver = webdriver.Chrome()
driver.get(url)

try:
    for _ in range(1):
        more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.more')))
        more_button.click()
        time.sleep(0.4)  # 1초 대기
        # 페이지의 모든 정보 가져오기
    page_source = driver.page_source

    card_imgs = []  # 이미지 링크를 저장할 배열
    card_links = []  # 카드 링크를 저장할 배열

    # BeautifulSoup을 사용하여 페이지 소스를 파싱
    soup = BeautifulSoup(page_source, 'html.parser')
    names = soup.select("b.name")
    descs = soup.select("p.desc")
    annual_fees = soup.select("i.annual_fee")

    links = soup.select("a.anchor")
    for link_tag in links:
        card_link = link_tag.get("href")
        card_links.append(card_link)
        
    imgs = soup.select("img.img")
    for img_tag in imgs:
        card_img = img_tag.get("src")
        card_imgs.append(card_img)
    
    # 텍스트만 추출하여 출력
    card_names = [element.text for element in names]
    card_descs = [element.text for element in descs]
    card_annual_fees = [element.text for element in annual_fees]

    # MySQL 데이터베이스에 연결
    # 메인 코드
    conn = pymysql.connect(host="127.0.0.1", user="root", password="sbkm8531*", db="moneyplant", charset="utf8")
    cursor = conn.cursor()
    
    # 크롤링한 결과를 MySQL에 저장
    for name, desc, img, link, annual_fee in zip(card_names, card_descs, card_imgs, card_links, card_annual_fees):
        # SQL 쿼리 실행
        query = "INSERT INTO card_list (card_name, card_category, card_desc, card_img, card_link, card_annual_fee) VALUES (%s, %s, %s, %s,%s,%s)"
        values = (name,'주거', desc, img, 'https://card-search.naver.com'+link, annual_fee)
        cursor.execute(query, values)

    # 변경 사항 저장
    conn.commit()

    # 연결 종료
    conn.close()

except TimeoutError:
    print('TimeOut')
finally:
    driver.quit()


# 의료
url = 'https://card-search.naver.com/list?benefitCategoryIds=21&sortMethod=ri&isRefetch=true&bizType=CPC'
driver = webdriver.Chrome()
driver.get(url)

try:
    for _ in range(5):
        more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.more')))
        more_button.click()
        time.sleep(0.4)  # 1초 대기
        # 페이지의 모든 정보 가져오기
    page_source = driver.page_source

    card_imgs = []  # 이미지 링크를 저장할 배열
    card_links = []  # 카드 링크를 저장할 배열

    # BeautifulSoup을 사용하여 페이지 소스를 파싱
    soup = BeautifulSoup(page_source, 'html.parser')
    names = soup.select("b.name")
    descs = soup.select("p.desc")
    annual_fees = soup.select("i.annual_fee")

    links = soup.select("a.anchor")
    for link_tag in links:
        card_link = link_tag.get("href")
        card_links.append(card_link)
        
    imgs = soup.select("img.img")
    for img_tag in imgs:
        card_img = img_tag.get("src")
        card_imgs.append(card_img)
    
    # 텍스트만 추출하여 출력
    card_names = [element.text for element in names]
    card_descs = [element.text for element in descs]
    card_annual_fees = [element.text for element in annual_fees]

    # MySQL 데이터베이스에 연결
    # 메인 코드
    conn = pymysql.connect(host="127.0.0.1", user="root", password="sbkm8531*", db="moneyplant", charset="utf8")
    cursor = conn.cursor()
    
    # 크롤링한 결과를 MySQL에 저장
    for name, desc, img, link, annual_fee in zip(card_names, card_descs, card_imgs, card_links, card_annual_fees):
        # SQL 쿼리 실행
        query = "INSERT INTO card_list (card_name, card_category, card_desc, card_img, card_link, card_annual_fee) VALUES (%s, %s, %s, %s,%s,%s)"
        values = (name,'의료', desc, img, 'https://card-search.naver.com'+link, annual_fee)
        cursor.execute(query, values)

    # 변경 사항 저장
    conn.commit()

    # 연결 종료
    conn.close()

except TimeoutError:
    print('TimeOut')
finally:
    driver.quit()


    
# 교육
url = 'https://card-search.naver.com/list?benefitCategoryIds=9&sortMethod=ri&isRefetch=true&bizType=CPC'
driver = webdriver.Chrome()
driver.get(url)

try:
    for _ in range(4):
        more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.more')))
        more_button.click()
        time.sleep(0.4)  # 1초 대기
        # 페이지의 모든 정보 가져오기
    page_source = driver.page_source

    card_imgs = []  # 이미지 링크를 저장할 배열
    card_links = []  # 카드 링크를 저장할 배열

    # BeautifulSoup을 사용하여 페이지 소스를 파싱
    soup = BeautifulSoup(page_source, 'html.parser')
    names = soup.select("b.name")
    descs = soup.select("p.desc")
    annual_fees = soup.select("i.annual_fee")

    links = soup.select("a.anchor")
    for link_tag in links:
        card_link = link_tag.get("href")
        card_links.append(card_link)
        
    imgs = soup.select("img.img")
    for img_tag in imgs:
        card_img = img_tag.get("src")
        card_imgs.append(card_img)
    
    # 텍스트만 추출하여 출력
    card_names = [element.text for element in names]
    card_descs = [element.text for element in descs]
    card_annual_fees = [element.text for element in annual_fees]

    # MySQL 데이터베이스에 연결
    # 메인 코드
    conn = pymysql.connect(host="127.0.0.1", user="root", password="sbkm8531*", db="moneyplant", charset="utf8")
    cursor = conn.cursor()
    
    # 크롤링한 결과를 MySQL에 저장
    for name, desc, img, link, annual_fee in zip(card_names, card_descs, card_imgs, card_links, card_annual_fees):
        # SQL 쿼리 실행
        query = "INSERT INTO card_list (card_name, card_category, card_desc, card_img, card_link, card_annual_fee) VALUES (%s, %s, %s, %s,%s,%s)"
        values = (name,'교육', desc, img, 'https://card-search.naver.com'+link, annual_fee)
        cursor.execute(query, values)

    # 변경 사항 저장
    conn.commit()

    # 연결 종료
    conn.close()

except TimeoutError:
    print('TimeOut')
finally:
    driver.quit()