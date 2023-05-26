# 고객의 이름 입력 받기
# 행사 제목 입력 받기
# 행사 날짜 입력 받기 : 날짜를 입력 받아 몇 월인지 확인하고 그에 맞는 행사 문구를 가져와 출력 
# 행사 시간 입력 받기 : 시간을 입력 받아 예쁘게 변경

# 한파의 연속인 1월 입니다.
# 봄을 기다리는 2월 입니다.
# 봄의 기운이 느껴지는 3월 입니다.
# 새싹이 피어나는 4월 입니다.
# 계절의 여왕 5월 입니다.  
# 활동하기 좋은 6월 입니다. 
# 휴가가 기다려지는 7월 입니다. 
# 무더운 8월 입니다. 
# 선선한 9월 입니다. 
# 천고마비의 계절 10월 입니다.
# 쓸쓸한 늦가을 11월 입니다.
# 올 한해의 마무리 12월 입니다.

#========================================================================================================

name = input("이름 : ")
event = input("제목 : ")
date = input("일시 : ")
time = input("시간 : ")

# date에서 몇월인지 가져오기
month = date[4:6]
greeting = "봄의 기운이 느껴지는 3월 입니다."

print(f"{name}님.")
print(greeting)
print(f"아래와 일정으로 {event}를 진행 하고자 하오니 오셔서 \
자리를 빛내 주시기 바랍니다.\n")
print("="*5, "행사 안내", "="*5)
print("행사 안내 : " + event)
# print("일시 : " + date[:4] + "년 " + date[4:6]+"월 " + date[6:8] + "일")
print(f"일시 : {date[:4]}년 {date[4:6]}월 {date[6:8]}일")
print("시간 : " + time + "시")

if month == "01":
    greeting = "한파의 연속인 1월 입니다."
elif month == "02":
    greeting = "봄을 기다리는 2월 입니다."
elif month == "03":
    greeting = "봄의 기운이 느껴지는 3월 입니다."
elif month == "04":
    greeting = "새싹이 피어나는 4월 입니다."
elif month == "05":
    greeting = "계절의 여왕 5월 입니다."
elif month == "06":
    greeting = "활동하기 좋은 6월 입니다."
elif month == "07":
    greeting = "휴가가 기다려지는 7월 입니다."
elif month == "08":
    greeting = "무더운 8월 입니다."
elif month == "09":
    greeting = "무더운 8월 입니다."
elif month == "10":
    greeting = "천고마비의 계절 10월 입니다."
elif month == "11":
    greeting = "쓸쓸한 늦가을 11월 입니다."
else :
    greeting = "올 한해의 마무리 12월 입니다."


trans_time = int(time)
if(trans_time > 12):
    trans_time = trans_time - 12
    time = "오후" + str(trans_time)
else:
    time = "오전" + str(trans_time)