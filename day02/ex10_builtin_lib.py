# ex10_builtin_lib.py 파이썬내장 라이브러리

# 라이브러리(모듈).클래스.함수() 나열
#import datetime
from datetime import datetime

# datetime 클래스 내 현재 일시 함수
# print(datetime.datetime.now())
curr = datetime.now()
print(curr)
print(curr.year)
print(curr.month)
print(curr.day)
print(curr.date())
print(curr.weekday())  # 몇번째 요일, 월0 ~ 일6

print(curr.hour)
print(curr.minute)
print(curr.second)
print(curr.microsecond)

print(curr.strftime('%Y/%m/%d %H:%M:%S'))