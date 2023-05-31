# 파이썬 기본 입출력 함수: input()/print()
# 사용자가 터미널에 대해 입출력이 아닌 파일에 대한 입출력하기 위해서는 파일에 대한 입출력에 대한 별도의 함수를 사용한다.
# 파일 쓰기 : 파일 객체 = open(파일명, 파일모드, 인코딩)

score_file = open("score.txt", "w", encoding="utf8")
# score_file = open("score.txt", "a", encoding="utf8") # append
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.write("과학 : 80" + "\n")
score_file.write("코딩 : 100" + "\n")
score_file.close()

# 파일 읽기
# read(): 파일 내의 모든 내용을 읽어 하나의 문자열로 반환
# readline() : 한 줄씩 내용을 읽고 EOF(End of file)에 도달시, None을 반환
# readlines() : 해당파일의 모든 라인을 순서대로 읽어 들인다.

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()

# with 키워드 : 프로그램이 길어지면 open과 close 사이에 많은 코드가 들어가 close를 호출하지 않는 문제 발생 가능
# with 구문 사용 시 구문 종료될 때 자동으로 파일 닫힘
with open('textfile.txt', 'r') as file:
    contents = file.read()

# 위 구문과 동일한 내용
file = open('textfile.txt', 'r')
contents = file.read()
file.close()

from datetime import datetime

with open("password.txt", "w") as f: 
    date = str(datetime.today().year) + str(datetime.today().month) \
        + str(datetime.today().day)
    while True:
        url = input("사이트 : ")
        if url == "exit": break
        my_str = url.replace("http://", "")
        my_str = my_str[:my_str.index(".")] # 슬라이싱, 처음부터 . 위치 미만까지
        password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + date + "!" + "jks"
        print("비밀번호 : " + password)# 각 사이트 비밀번호 자동으로 만들기
        f.write(password + "\n")