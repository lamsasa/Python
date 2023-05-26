# while문 : 조건이 참인 동안 반복 수행하며 주로 횟수가 정해지지 않은 경우에 사용, 횟수가 정해지지 않은 경우 반드시 탈출 조건이 필요
n = int(input("정수 입력 : "))
sum = 0
while n : 
    sum += n
    n -= 1

    print(sum)

# 유효값 체크

# for 변수 in range(시작, 종료, 증감값) : 자바의 기본적인 for과 동일
n = int(input("정수 입력 : "))
sum = 0
for i in range(1, n+1) : 
    sum += i

print(sum)