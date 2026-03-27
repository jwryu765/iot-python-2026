## pr01_vending.py 자판기 프로그램

menu = ['칠성사이다', '펩시콜라', '코카콜라', '제로콜라', '웰치스', '백산수']
price = [1900, 2100, 2200, 2000, 2300, 1000]
money = 0
sel = 0

def printmenu():
    print('[자판기 메뉴]')
    for i in range(0, len(menu)):
        print(f'{i+1}. {menu[i]}\t가격 : {price[i]}')
    print()

def getproduct(num):
    if money < price[num]:
        print(f'잔액부족, 잔액 : {money}원')
        return money
    else:
        print(f'{menu[num]} 구입완료!')
        balance = money - price[num]  # 5000 - 2200 = 2800(balance)
        print(f'잔액 : {balance}원')
        return balance

money = int(input('지폐를 투입하세요 > '))

while True:  # while (1) {}
    printmenu()
    sel = int(input('메뉴번호 선택 (종료: 0) '))

    if sel == 0:
        break
    elif (sel >= 1 and sel <= len(menu)):
        print(f'{menu[sel-1]} 선택!')
        money = getproduct(sel-1)
    else:
        print('메뉴선택 다시해요')

print('자판기 사용 끝')