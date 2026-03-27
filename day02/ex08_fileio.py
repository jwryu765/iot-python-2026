# ex08_fileio.py 파일 입출력
# 인코딩 주의

print('파일 입출력')

# 파일쓰기
## 파일 경로 주의요망!
f = open('./day02/test.txt', 'w')  # 쓰기 모드로 파일 오픈
# with open('test.txt', 'w') as f:
f.write('텍스트를 한줄 씁니다.\n')
f.write('텍스트를 두줄 씁니다.\n')

f.close()

# with open('test.txt', 'w') as f:  # with를 사용하면 close() 생략가능
with open('./day02/test.txt', 'r') as f:
    content = f.read()
    print(content)