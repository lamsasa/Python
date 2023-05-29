# 연속적으로 데이터를 저장하는 자료형, 동적으로 크기가 변경됨. 다른 타입의 데이터를 함께 사용 가능(다른 배열, 다른 타입)
# 읽고 쓰기가 가능, []

numbers = [1,2,3,4,5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "apple", True, 3.14, [1,2,3,4,5]]

empty = []
str_n = ""

## 변수 사용 대비 이점
#kor, eng, mat = map(int, input("성적 입력 : ").split())
#tot = kor + eng + mat
#print(f"평균 : {tot/3}")

#score = list(map(int, input("성적 입력 : ").split()))
#print(f"평균 : {sum(score)/len(score)}")
#print(mixed)

s = ["korea", "seoul", "inchun", [1,2,3,4,5], ["안유진", "장원영", "가을", "이서", "리즈"]]
print(s[0][1])
print(s[3][4])
print(s[4][1][1])

# 리스트 연산자 : 연결(+), 반복(*)
list_a = [1,2,3]
list_b = [4,5,6]
print(list_a *3)
print(list_b + list_a)

# 리스트 요소 추가
# append : 리스트의 끝에 값을 추가하는 함수
# insert : 특정 위치에 값을 추가하는 함수