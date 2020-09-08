"""
有一个银行账户类 Account 包括名字，余额等属性，方法有存钱，取钱，查询余额的操作，要求:
    1.在存钱时，注意存款数据的格式
    2.取钱时，要判断余额是否充足，余额不够的时候要提示余额不足
"""


class Account:
    def __init__(self, name, balance=0):
        super().__init__()
        self.name = name
        self.balance = balance

    def save_money(self, x):
        if type(self.balance) == int:
            self.balance += x
            print('成功存取{}'.format(self.balance))
        else:
            print('你存取的格式不对')

    def take_money(self, x):
        self.balance -= x
        if self.balance <= 0:
            print('提取{}'.format(x))
            print('抱歉,您的余额不足')
            self.balance += x

    def check_balance(self):
        print(self.balance)


acc1 = Account('lisa')
acc1.save_money(5000)
acc1.take_money(6000)
acc1.check_balance()
