# 함수? 특별한 목적을 수행하기 위해 독립적으로 설계된 프로그램을 의미
# 함수의 사용 목적은 재사용성과 모듈화를 위해 사용

# 은행 계좌 개설 및 입금, 출금 예제
def open_account(name) : 
    print(f"{name}님의 계좌가 개설되었습니다.")
    return name

# 입금
def deposit(balance, input) : 
    print(f"{input}이 입금되었습니다. 잔액은 {balance + input}입니다.")
    return balance + input

#출금
def withdraw(balance, input) :
    if balance >= input :
        print(f"{input}이 출금되었습니다. 잔액은 {balance - input}입니다.")
        return balance - input
    else :
        print(f"잔액이 부족해 출금에 실패하셨습니다.")
        return balance

# balance = 0 # 외부에서 선언하지만 매개변수로 전달 함
# name = open_account("mmm")
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# print(f"{name}님의 잔액은 {balance}입니다.")

# # 기본값 인자 : 함수 선언 시 매개변수에 대한 기본 값을 정의할 수 있습니다.
# def profile(name, year = 2, age = 18, school ="태양고") :
#     print(f"이름 : {name}, 학교 : {school}, 학번 : {year}, 나이 : {age}")
# 
# profile("나희도")
# profile("고유림")
# profile("백이진", None, 22)

# 가변 매개 변수 : 함수의 매개변수 앞에 (*) 붙여주면, 함수 매개변수를 몇 개 입력하던 함수 내에서 튜플로 인식
def profile(name, age, *lang) :
    print(f"이름 : {name}, age : {age}", end=" ")
    for e in lang :
        print(e, end=" ")
# profile("강호동", 18, "Python", "Java", "C", "C++", "React", "Kotlin")
# profile("조세호", 38, "Python", "Java")
# profile("유재석", 48, "Python", "Java", "C", "C++")

# 지역 변수와 전역 변수
# 전역 변수 : 함수보다 변수의 생존범위가 더 넓어서 리턴 값이 필요없음
# golbal 키워드 사용시 전역으로 선언한 변수를 함수내에서 사용 불가

knife = 10 # 칼을 10자루 준비
def game(player) :
    global knife
    knife -= player # 게임에서 참가한 선수가 사용한 개수만큼 차감
    
def game2(player, knife) :
    knife -= player
    print(f"남아 있는 칼은 {knife}자루 입니다.")

player = int(input("경기에 참여하는 선수가 몇 명 입니까?"))
game2(player, knife)

# 람다와 함수
# 람다란? 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현, 이름 없는 함수를 의미
def add(a, b) :
    return a + b

# print(add(10, 20))
# print((lambda a, b : a+b)(10, 20))

def power(n) :
    return n*n

square = lambda x:x*x # 람다식으로 익명의 함수 만들기
input = [1,2,3,4,5,6,7,8,9,10]

output = list(map(lambda x:x*x, input))
print(output)