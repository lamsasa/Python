# 이름 입력
# 나이 입력 : 1~199까지 입력 받고 잘못된 값이 오면 재입력 요청을 한다.
# 성별 입력 : 영문자 (M과 m은 남성),  (F, f 여성)으로 입력 받고 나머지는 재입력을 요청한다.
# 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재압력을 요청한다.
# 결과는 마지막에 한 번에 출력한다.

name = input(print("이름 입력 : "))
age = input(print("나이 입력 : "))
sex = input(print("성별 입력 : "))
job = input(print("직업 입력 : "))
print("이름" + {name}, "나이" + {age}, sex, job)
