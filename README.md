# iot-python-2026
IoT 개발자 파이썬 리포지토리

## 1일차

### 사전 정리

사전 C/C++ 학습완료. 프로그래밍 문법 파악 중

**기본 문법 리스트**
- 변수, 데이터형
- 연산자
- 제어문
    - 조건문
    - 반복문
- 함수/메서드
- 배열 개념 - 리스트
- 포인터/참조 개념 - 포인터없음
- 구조체 - 구조체 없음
- 파일 입출력
- 객체지향 클래스
- 예외처리

다른 언어는 새로 다시 공부해야 한다보다, 필요한 것만 보충 학습하겠다고 생각할 것

### 이론적 개념 정리

#### 파이썬에서 신경 안써도 되는 것
- 학습 난이도를 낮추는 목록
    - 자료형 선언 안 함
    - 세미콜론 없음(옵션으로 사용 가능)
    - 중괄호 없음 - `들여쓰기를 신중히`
    - `int main()` 강제 아님 - 비슷한 기능은 있음
    - 메모리 할당/해제 거의 안 함
    - 헤더 파일 개념 없음
    - 컴파일 과정 신경 거의 안 씀
    - 개발환경 설정 어렵지 않다

- 문법 비교표

    |이론개념|C/C++|Python|
    | --- | --- | --- |
    | 출력 | printf(), cout | `print()` |
    | 변수 선언 | int a = 10; | `a = 10` |
    | 조건문 | if (a > b) { ... } | `if a > b:` |
    | 반복문 | for (int i = 0; i < 10; i++>) {} | `for i in range(10):` |
    | 함수 | int add(int a, int b) {} | `def add(a, b):` |
    | 배열 | int arr[5] | `list` |
    | 문자/문자열 | char, char[], char*, string | `str` |

- `장점`
    - 들여쓰기가 코드 블록, {} 불필요
    - 선언이 없음
    - 리스트가 배열보다 훨씬 편하고 간결
    - 문자열 처리 간단
    - 함수 만들기 간단

- 단점
    - 들여쓰기 문제 가능성(공백하나로도 문법오류)
    - 파일명 지정 시 클래스명과 동일하게 사용하면 문제발생
    - 디버그 콘솔이 여러개 실행 가능(하나만 실행되도록 정리)

    ![alt text](image-6.png)

    ![alt text](image-7.png)

### 파이썬 설치

- http://python.org - 다운로드
    - 최신버전 설치 지양. 3.12 버전
    - ~~Python install manager 클릭~~
    
    ![alt text](image.png)

    - 3.12 페이지 검색, Windows installer (64-bit) 클릭

- 설치
    - 아래와 같이 설치

    ![alt text](image-1.png)

    - 다음에서 Documentation 만 체크 해제
    - Advanced Options에서 Install Python 3.12 for all users 활성화
    - Install 시작
    - 설치 후

    ![alt text](image-2.png)

    - 윈도우 디렉토리 Path 길이 260자 제한되어 있음. Linux/MacOS 등과 호환시 문제 발생
    
    - 콘솔에서 확인 안되면 시스템 속성(sysdm.cpl) 에서 Path 확인할 것

    ![alt text](image-3.png)

### VS Code 확장
- 확장
    - Python으로 검색 후 설치

    ![alt text](image-4.png)


    - Jupyter 검색 후 설치

    ![alt text](image-5.png)

### 깃허브 확장
- 웹 코딩 환경
    - https://github.com -> com을 dev로 변경 실행
    - Visual Studio Code와 동일한 화면으로 변경
    - 주피터 노트북으로 데이터분석 등을 깃허브에서 바로 개발할 때 활용
    - Google Colab과 동일

    ![alt text](image-8.png)


### 파이썬 기본 학습

1. 기본 입출력 - [소스](./day01/ex01_basicoutput.py)
    - .py 파일 작성
    - Ctrl + F5 실행
    - 디버거 선택 > Python Debugger 선택

2. 리스트(배열 대체) - [소스](./day01/ex02_array.py)
    - 어떤 데이터타입도 추가 가능
    - append ~ sort 까지 11개 함수만 학습

3. 제어문 - [소스](./day01/ex03_logic_control.py)
    - if, for
    - switch~case 문 없음

## 2일차

### 파이썬 기본 학습

4. 변수, 자료형 - [소스](./day02/ex04_variable.py)
    - 선언이 없고 자료형을 지정안함
    - 자료형 자체를 사용안함, 형변환 필요
    - 기본자료형, int, float, str, bool, None Type(NULL과 거의 똑같은 기능)

5. 연산자 - [소스](./day02/ex05_operator.py)
    - 사칙연산, 할당연산, 비교연산, 논리연산, 멤버십연산
    - 연산자 우선순위 : 거듭제곱 > 곱셈/나눗셈 > 덧셈/뺄셈, ()로 연산자 우선순위 설정

6. 문자열 - [소스](./day02/ex06_string.py)
    - C방식 문자열 처리가능
    - 여러 문자열 출력방식 존재, f-string 사용추천
    - 포맷팅 기법

7. 함수 - [소스](./day02/ex07_function.py)
    - 객체지향언어 함수 -> 메서드(Method)로 호칭(C#, Java, ...)
    - 파이썬도 함수(Function)으로 호칭
    - C와 유사하게 함수 사용 전에 선언
    - def로 선언 파라미터 괄호 뒤 : 사용

8. 파일 입출력 - [소스](./day02/ex08_fileio.py)
        - C/C++과 모드가 동일 r, w, a
        - with 구문으로 close() 생략 가능
        - 쓰기 각 문장끝 '\n' 추가
        - 기본적으로 UTF-8
        - CSV, JSON, 텍스트파일 등 읽기에 많이 사용

9. 여기까지 배우고 활용하는 분야도 존재
        - 데이터분석, 머신러닝,딥러닝, ...

10. 연습
    - 구구단 - [소스](./day02/pr01_gugudan.py)
    - 자판기 - [소스](./day02/pr02_vending.py)

11. 외부 라이브러리 사용 - [소스](./day02/ex10_builtin_lib.py)
    - 파이썬 표준 라이브러리 - 파이썬에 포함된 기본 라이브러리
    - 외부 라이브러리 - pip로 설치하는 3rd-party에서 개발된 라이브러리
    - C/C++ `include` -> python `import`
    - import : 모듈과 클래스를 모두 기재
    - from ~ import ~ : 클래스명만 기재
    - 라이브러리(모듈).클래스.함수() 형태로 존재

13. 가상환경

14. 객체지향

15. 예외처리

16. main

### 파일 입출력
- 인코딩
    - EUC-KR : 2바이트 한글 완성형 인코딩. CP949 동일한 의미
    - UTF-8 : 1바이트 영문(ASCII호환), 3바이트 한글, 4바이트 이모지 등 최대 4바이트 사용 국제어표준
    - 대한민국 데이터 포털 제공하는 CSV는 EUC-KR 사용중. UTF-8 변환필요

- csv
    - 엑셀과 호환가능한 텍스트파일
    - 텍스트 양이 많으면 한번에 읽을 수 없음. 한줄씩 나눠서 읽어야 함
    - 보통 csv 라이브러리 사용

- JSON
    - Javasript Object Notation : 자바스크립트에서 데이터를 사용하기 위해 만든 표기방법
    - 딕셔너리를 텍스트화
    - 데이터를 네트워크로 전달할때 가장 효율적인 파일형식
    - XML을 대체하는 기술
    - 저장된 json 파일을 사용 또는 OpenAPI 네트워크로 전달된 데이터를 사용