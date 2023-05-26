# 입력 받은 n개의 원소에 대한 평균 구하기

# 정수 n을 입력 받아 n*n 출력
# n개에 대한 숫자를 입력 받아 최소 최대 구하기
# 주민번호를 입력 받아 생년월일, 성별, 나이 출력
# 알람 설정하기


# 별 찍기
n = int(input())
for i in range(n) :
    for j in range(i + 1) :
        print("*", end= "")
    print()


#----------------------------------------

n= int(input())
for i in range(n) :
    for j in range(n-i) :
        print("*", end= "")
    print()

#--------------------------------------------

n= int(input())
for i in range(n) :
    for j in range(n) :
        print("*", end= "")
    print()

# for문으로 알파벳 출력하기
# chr : 유니코드의 값을 입력 받아 코드에 해당하는 문자 출력
# ord : 문자의 유니코드 값을 돌려주는 함수
# for i in range (ord("A"), ord("Z")+1) :
#       print(chr(i, end=" "))

# for i in range(65, 90+1) : 
#       print(chr(i), end=" ")

# 학점 구하기 : 성적을 입력 받아 학점 출력하기
while True :
    score = int(input("점수 입력 : "))
    # 종료 조건
    if score < 0 : break
    # 재입력 요구 조건
    if score > 100 : 
        print("점수를 잘못 입력하셨습니다.")
        continue
    if score >= 90 : grade ="A"
    elif score >= 80 : grade = "B"
    elif score >= 70 : grade = "C"
    elif score >= 60 : grade = "D"
    else : grade = "F"

    print(f"{score}에 대한 학점은 \"{grade}\"입니다.")