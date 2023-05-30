# 튜플? 변경할 수 없는 시퀀스 자료형, ()괄호를 사용해 생성
# 패킹과 언패킹 개념이 있다.
# 튜플 정의하기
person = ("bear", 25, "seoul") # ()괄호 생략해도 튜플, 쓰기 불가 특성
# person = "bear", 25, "seoul", True = 얘도 튜플
# person[0] = "change another name" => 변경 불가
print(person)

# 튜플 unpacking(구조분해와 유사)
name, age, city = person
print(name)
print(age)
print(city)

# 튜플을 이용한 함수 반환값 다루기
def get_person() :
    name = "myname"
    age = 25
    city = "suwon"
    return name, age, city
# result = get_person()
# print(result)

a, b, c = get_person()
# print(a, b, c)

# 기본적인 동작
tp = 1,2,3,4,5,6,7,8,9,10,1,1,2,2,3,3
print(tp.count(3)) # 원하는 데이터의 개수를 세어주는 함수(리스트와 동일)
print(tp.index(1)) # 원하는 데이터의 시작 인덱스를 알려주는 함수
print(len(tp)) # 튜플에 포함된 데이터의 개수
print(tp.__len__())

# 튜플에서 사용 불가(삭제는 안 됨)
t1 = 1,2,3,4,5
# del t1[0] => 삭제 불가
