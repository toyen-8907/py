# 物件導向程式設計中類別是可以繼承的，被繼承的類別 >>> 父類別、基底類別、超類別
# 繼承的類別 >>> 子類別、衍生類別
# 繼承的優點 類別的公有方法或屬性，不用重新設計，可以直接被子類別引用
# 先定義基底類別
# 再定義衍生類別
'''
class Father():
    def acting(self):
        print("我在學程式")


class Son(Father):
    pass


hung = Father()
ivan = Son()
hung.acting()
ivan.acting()
'''

# 如何取得基底類別得私有屬性


class Father():
    def __init__(self):
        self.__address = "台北市中山區"

    def getaddress(self):
        return self.__address


class Son(Father):
    pass


a = Father()
b = Son()
print("父類別 : ", a.getaddress())
print("子類別 : ", b.getaddress())


class Banks():
    # 初始值通常設在 __init__()方法內
    def __init__(self, uname):
        self.__name = uname
        self.__balance = 10000
        self.__bankname = "taipei bank"

    def save_money(self, money):
        self.__balance += money
        print("存款", money, "complete")

    def withdraw_money(self, money):
        self.__balance -= money
        print("提款%d完成" % money)

    def get_balance(self):
        print(self.__name.title(), "目前餘額:", self.__balance)

    def bank_title(self):
        return self.__bankname


class SHILIN_bANKS(Banks):
    # 定義士林分行
    def __init__(self, uname):
        self.bankname = "taipei bank - shilin branch"


jamesbank = Banks("james")
print("james's banks = ", jamesbank.bank_title())
hungbank = SHILIN_bANKS("hung")
print("hung's banks = ", hungbank.bankname)

# 衍生類別與基底類別有相同名稱的屬性


class Person():
    def __init__(self, name):
        Person.name = name

    @classmethod
    def get_sd(cls):
        print(cls.name)


class Lawerperson(Person):
    def __init__(self, name):
        self.name = name + "律師"


hung = Person("cty")
lawer = Lawerperson("cy")
hung.get_sd()
print(lawer.name)
