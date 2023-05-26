# 중복값이 없는 로또 번호 생성
import random
print("lotto 번호 자동 생성  : ", end="")
ls =[]
while True :
    rand = random.randrange(1, 46)
    if rand not in ls :
        ls.append(rand)
    if len(ls) == 6 : break
print(ls)