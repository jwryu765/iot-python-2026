## ex14_main.py  메인 함수 개념

# __name__ 파이썬의 특별 변수(Special variable)
# __import__ 와 같은 특별 함수(Special method)
# dunder(double underscore) : _ 가 두 개씩 붙은 키워드

# 개발자가 사용하는 것 __name__, __init__, __str__ 등 몇가지만 사용

if __name__ == '__main__':  # int main()와 동일 기능
    print('프로그램 시작')
    print(__name__)