# 입력 받은 수가 소수인지 아닌지 판별하기(함수 이용)
num = int(input("정수를 입력해주세요. : "))

def is_prime(num) :
    for i in range(2, num) : # 1과 자기자신 제외
        if num%i == 0 : return False
    return True

if(is_prime(num)) : print(f"{num}은 소수이다.")
else : print(f"{num}은 소수가 아니다.")