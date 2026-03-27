## pr01_gugudan.py 구구단 프로그램

# 2중 for문

dan = int(input('출력 최대단 수(2~9) > '))

for i in range(2, dan + 1):
    print(f'{i}단 출력')
    

    for j in range(1, 9 + 1):
        print(f'{i} x {j} = {i*j:>2}', end=' ')
    print()