## ex12_csv_package.py  csv 패키지(모듈) 사용 CSV파일 읽기
import csv   # 기본 라이브러리(패키지)

with open('./day02/부산시_해운대구_도서정보.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)

    for row in reader:  # 리더를 한줄씩 읽어서 끝까지
        print(row) # 한 줄씩 리스트로 출력