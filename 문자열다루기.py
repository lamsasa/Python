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

#갯수세기: count

# 문자열 찾기 : find(), rfind(), index()
# find(): 찾은 문자열의 첫번째 인덱스 반환, 문자열을 차지 못하면 -1 반환
# index() : 찾은 문자열의 첫 번째 인덱스 반환, 문자열을 차지 못하면, valueError 예외 발생

phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장")) # 뒤에서 부터 찾지만 인덱스는 앞에서 부터

print(phrase.index("포기")) 

print(phrase.find("나에게"))  # 찾는 결과 없으면 -1
# print(input_b.index("나에게")) # 해당 단어가 없으므로 에러가 발생 합니다

new_phrase = phrase.replace("가장", "나에게")
print(new_phrase)

# 문자열 연산자
# "문자열" + "문자열"
# "문자열" *3 : 뒤에 오는 숫자만큼 문자열을 반복
print("태양고" *2)
print("안녕하세요", "!"*5, "\n", "\t", "=" *3, "\nggg"*3, "입니다.")