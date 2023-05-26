# 조건문 : if ~ else
num = int(input("정수 입력 : "))
if num % 2 == 0 :
    print("짝수입니다.")
else : 
    print("홀수다.")



# 조건문 : if ~ elif ~else
n = int(input("정수 입력 : "))
if n> 100 : 
    print("100보다 크다")
elif n <100 :
    print("100보다 작다")
else :
    print("100")



print("지금 계절? : ", end = '')
season = input()
if season == "spring" : print("봄이 왔어요")
elif season == "summer" : print("여름이 왔어요")
elif season == "fall" or season : "autumn" : print("가을이 왔어요")
elif season == "winter" : print("겨울이 왔어요")
else : pass





#age = int(input("나이를 입력하세요 : "))

#if(0< age<200) : 
#    print("정상")
#else: 
#    print("오류")


# 회원 가입 위한 아이디, 패스워드 입력 받기
# string.find(찾을 문자)
# string.find(찾을 문자, 시작 인덱스)
# string.find(찾을 문자, 시작 인덱스, 끝 인덱스)
# 회원 가입을 위한 아디와 패스워드 입력 받기
user = input("아이디 입력 :")
if len(user) >= 10:
    pw = input("비밀번호 입력 : ")
    if pw.__len__() < 8 or pw.__len__() > 16:
    # if len(pw) < 8 or len(pw) > 16:   # 조건식 생략이 안된다. 범위가 다르기 때문..
        print("비밀번호는 8자에서 16자 사이여야합니다")
    elif pw.find(user) >= 0:  # 없으면 -1을 반환 합니다.
        print("비밀번호에 아이디를 포함시킬 수 없습니다")
    else:
        print("아이디 : {}".format(user))
        print("비밀번호 : {}".format(pw))
else:
    print("아이디는 반드시 10자리 이상이여야합니다")