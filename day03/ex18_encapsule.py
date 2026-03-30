## ex18_encapsule.py 캡슐화

class Account:
    def __init__(self, money):
        # self.balance = money # self.balance는 public 접근과 공일
        self.get_balance = money  # __ 는 private과 동일

    def deposit(self, money):  # 계좌임금
        self.balance += money

    def get_balance(self):  # 계좌조회 getter
        return self.balance


if __name__ == '__main__':
    myacc = Account(1000000)
    print(f'계좌금액은 {myacc.get_balance():,}원')
    print(f'계좌금액 : {myacc.balance:,}달러')

    myacc.deposit(100_000)  # 정수를 사용시 _로 1000단위 구분가능
    print(f'계좌금액은 {myacc.get_balance():,}원')

    myacc.balance= -100000000  # 멤버변수에 직접접근가능
    print(f'계좌금액은 {myacc.get_balance():,}원')