# 산술 연산자 : 더하기, 빼기, 곱하기, 나누기, 나머지, 몫
i, j = 10, 3

print("%d + %d = %d"%(i, j, i+j))
print("%d - %d = %d"%(i, j, i-j))
print("%d * %d = %d"%(i, j, i*j))
print("%d / %d = %d"%(i, j, i/j))

print(i/j) # 나누기 연산자
print(i//j) # 몫 연산자
print(i**j) # 제곱 연산자

# tax_rate = 0.10
#income = int(input("Input your income :"))
# print(f"당신의 연봉은 {month_pay * 12 * 1.15 : 2f}")

tax_rate = 0.10
income = int(input("당신의 수입은 얼마입니까? "))
print(f"당신이 내야 할 세금은 {income * tax_rate} 입니다.")


# 관계 연산자 대부분 비교 연산자와 함께 사용, 참 거짓 판별
# and, or, not(현재 결과 부정)
x = 10
y = 20
z = 30

result1 = (x > 0) and (x < y)
result2 = (x > 0) or (x > y) 
result3 = not((x > 0) or (x > y))

print(result1, result2, result3)

# 나머지 연산자와 다항 연산자
# (조건) and 참인 경우 or 거짓인 경우
num = int(input("정수 입력 : "))
flag = (num % 2 == 0) and "짝" or "홀"
print(f"임력하신 숫자는 {flag}입니다.")

age = 23
is_adult = (age >= 20) and "성인" or "미성년자"
print(is_adult)