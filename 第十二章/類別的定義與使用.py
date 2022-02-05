class Banks():
    '''定義銀行類別'''
    bankname = "taipei bank"
    # 初始值通常設在 __init__()方法內

    def __init__(self, uname):
        self.name = uname
        self.balance = 10000

    def save_money(self, money):
        self.balance += money
        print("存款", money, "complete")

    def withdraw_money(self, money):
        self.balance -= money
        print("提款%d完成" % money)

    def get_balance(self):
        print(self.name.title(), "目前餘額:", self.balance)


hungbank = Banks("hung")
hungbank.get_balance()
hungbank.save_money(12344)
hungbank.get_balance()
hungbank.withdraw_money(1344)
hungbank.get_balance()

jongbank = Banks("jong")
jongbank.withdraw_money(2400)
jongbank.get_balance()
