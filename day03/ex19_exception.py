## ex19_exception.py 예외처리

# 예외가 발생할 것으로 추측되면 위치를 try로 감싼다
try:
    num = int(input('나눌 분모 입력 > '))

    res = 100 / num
    print(f'100/{num} = {res}')
   
except ZeroDivisionError as e:  # 0으로 나눌때와
    print('0은 쓰지 마세요')
except ValueError as e:  # 숫자대신 문자를 입력할 때 예외를 나눠서 처리
    print('숫자만 넣으세요')
    
except Exception as e:  # 예외클래스 인스턴스 e 생성
    print(e.args)
else:  # 예외가 발생 안했을때만 처리
    print('프로그램 정상 종료') # 정상적으로 종료되면 출력
finally: # 옵션
    print('예외 유무관계 없이 실행')
    
print('끝!!')