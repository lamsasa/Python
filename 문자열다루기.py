# 작은 따옴표 3개를 사용해도 동일 : 여러 줄로 이뤄진 문자열 처리 시
print('''가나다라
마바사
아자차카''')
print("hello world")

# 이스케이프 문자 사용하기
print("서울시\t강남구\t역삼동")
print("사과\r바나나\r오렌지")

# 인덱싱 (슬라이싱(?)) : 인덱스 항상 0부터 시작
jumin = "020101-1111222"

print("성별 : " + jumin[7]) # 1은 남성
print("태어난 연도 : " + jumin[:2]) # 시작 인덱스를 주지 않으면 0에서 시작하고 end는 미만
print("월 : " + jumin[2:4]) # 2에서 4 미만

print("생년월일 : " + jumin[:6])
print("뒤 7자리" + jumin[7:])
print("뒤 7자리" + jumin[-7:])

print("안녕하세요"[0])
print("안녕하세요"[:2])
print("안녕하세요"[-3:])
print("안녕하세요"[7:]) # 아무거또 안 뜬다

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

# a[1] = "K" 문자열 요소는 변경 불가

# 대소문자 변경
a = "Hello Python Program.."
print(a.upper())
print(a.lower())

# 문자열 변경하기 : replace("","")
input_str = "Hello Python Program"
new_str = input_str.replace("Python", "React")
print(input_str)