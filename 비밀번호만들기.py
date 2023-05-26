#규칙1 : http://naver.com에서 앞의 http:// 잘라내기
#규칙2 : 처음 만나는 점(.) 이후 제외
#규칙3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자에 포함 된 'k'개수 + '!' + 자신의 이니셜

file_name = "password.txt"
f = open(file_name,"wt")
while True :
    url = input("사이트 : ")
    my_str = url.replace("http://","") #http:// 잘라내기
    my_str = my_str[:my_str.index(".")] # 슬라이싱, 처음부터 . 위치 미만까지
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("o")) + "!" + "jks"
    print("비밀번호 : " + password)# 각 사이트 비밀번호 자동으로 만들기
