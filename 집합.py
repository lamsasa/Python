# 집합? 주로 다른 자료형을 중복 제거할 때 자주 사용
# 순서가 없고 중복이 불가능하며, mutable(읽기, 쓰기) 특성

# 중복 제거
s1 = set([1,2,3,4,5,1,2,3,4,5,1,3,4,5])
print(s1)

s2 = set([1,2,3,4,5])
s3 = set([1,3,7,5,8,9])
# 교집합 : 양 쪽에 모두 존재하는 요소만 선택
print(s2.intersection(s3)) # *list는 교집합 안 먹힘

# 합집합
print(s2.union(s3))

# 차집합
print(s2.difference(s3))

# 중복 제거로 로또 번호 만들기
import random
lotto = set()
while True : # 무한의 반복을 돌릴 필요가 없다
    num = random.randrange(1, 46)
    lotto.add(num)
    if len(lotto) == 6 : break

print(lotto)