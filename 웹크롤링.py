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
