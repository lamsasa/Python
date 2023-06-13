# 웹페이지로부터 데이터를 추출하는 행위를 크롤링
# Beautiful Soup은 HTML및 XML 문서를 파싱하고 데이터를 추출하는 파이썬 라이브러리
from bs4 import BeautifulSoup

html = '''
<html>
    <table border=1> 
        <tr>
            <td> 항목 </td> 
            <td> 2013 </td> 
            <td> 2014 </td> 
            <td> 2015 </td>
        </tr> 
        <tr>
            <td> 매출액 </td> 
            <td> 100 </td> 
            <td> 200 </td>
            <td> 300 </td>
        </tr> 
    </table>
</html> 
'''
soup = BeautifulSoup(html, 'html.parser') 
result = soup.select('td') 
print(result)

# 각 태그의 텍스트만 가져오기
for val in result :
    print(val.text)

# 파이썬에서 HTTP 요청과 응답을 제공
import requests
res = requests.get("http://naver.com");
print("응답 코드 : ", res.status_code)

if res.status_code == requests.codes.ok:
    print("정상 입니다.")
else : 
    print("네트워크 오류 : [에러코드 ", res.status_code, "]");


# 타이틀 태그 검색
title_tag = soup.title
print(title_tag)  # <title>Example Page</title>

# 클래스가 "content"인 div 태그 검색
div_tags = soup.select('div.content')
for div in div_tags:
    print(div)  # <div class="content">...</div>

# href 속성이 있는 모든 a 태그 검색
a_tags = soup.find_all('a', href=True)
for a in a_tags:
    print(a)  # <a href="https://www.example.com">Link</a>

# 클래스가 "example"인 div 태그 검색
div_tags = soup.select('div.example')

# id가 "main"인 요소 검색
element = soup.select_one('#main')

# 자식 태그 검색
children = soup.select('#parent > .child')

# 형제 태그 검색
siblings = soup.select('.sibling ~ .sibling')