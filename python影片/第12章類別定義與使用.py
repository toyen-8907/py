class Banks:
    '''定義銀行類別'''
    bankname = "taipei bank"

    def __init__(self, uname, money):
        self.name = uname
        self.balance = money

    def get_balance(self):
        return self.balance


hungbank = Banks("hung", 100)


print(hungbank.name.title(), "存款餘額為:", hungbank.get_balance())
