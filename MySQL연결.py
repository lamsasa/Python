import pymysql

# 전역 변수
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

# MySQL 연결
conn = pymysql.connect(host="127.0.0.1", user="root", passwd="sbkm8531*", db="mysqlDB", charset="utf8")

# 커서 생성하기
cur = conn.cursor()

# # 테이블 생성
# cur.execute("CREATE TABLE userTable (id char(10), userName char(15), email char(20), birthYear int)")
 
# # 데이터 입력 하기
# cur.execute("INSERT INTO userTable VALUES('ayj', '안유진', 'ayj@gmail.com', 2003)")
# cur.execute("INSERT INTO userTable VALUES('jwy', '장원영', 'jwy@gmail.com', 2004)")

while(True) : 
    data1 = input("아이디 : ")
    if data1 == "" : break;
    data2 = input("이름 : ")
    data3 = input("이메일 : ")
    data4 = input("출생연도 : ")
    sql = "INSERT INTO userTable VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', '" + data4 + "')"
    cur.execute(sql)

# 데이터 저장하기
conn.commit()

# 연결 종료하기
conn.close()