# 객체 소속이 아니고 클래스 소속 메소드

class Person :
    count = 0
    def __init__(self) :
        Person.count += 1

    @classmethod
    def print_count(cls) : #cls로 클래스 속성에 접근
        print(f"{cls.count}마리 생성")

bear1 = Person()
bear2 = Person()

Person.print_count()
