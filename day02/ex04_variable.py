# ex04_variable.py 변수/자료형

# 여러줄 주석은 여러줄 문자열로 대체 사용
'''
여러줄 문자열을
주석처럼 사용

**자료형**
- 정수(int) : 10
- 실수(float) : 3.141592
- 문자열(str) : "Hello", 'Hello'
- 불린(bool) : True/False
- None(NoneType) : 
- 그 외 클래스 타입
'''

# val = "'Hello'" # 특수문자 \n, \t, \', \" 지원
# val = 10
# val = 3.14
# val = [1,2,3,4]
# val = ...
# val = True
val = None
print(val)
print(type(val))

age = 20 # int
print('나이는 ' * age)   # 문자열을 age의 값 만큼 반복
print('나이는' + str(age))  # 문자열을 다른 변수와 합치기(concatnate)
print('나이는 ', age, ' 입니다') # 여러값을 자동으로 합쳐서 출력하라

# 한글로 변수명 지정해도 됨, C/C++ 동일
이름 = input('이름 > ')
나이 = int(input('나이 > '))
키 = float(input('키 > '))

print('이름 : ', 이름, ',나이 : ', 나이, ', 키 : ', 키)
