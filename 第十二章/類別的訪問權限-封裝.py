# 公有屬性 --- 可以讓外部引用
# 私有屬性 --- 類別外無法呼叫，此概念又稱封裝
# 私有方法
class Banks():
    '''定義銀行類別'''
    # 初始值通常設在 __init__()方法內
    # 宣告時在屬性面前增加 __(兩個底線)，宣告維斯有屬性之後，類別外程式無法引用

    def __init__(self, uname):
        self.__name = uname
        self.__balance = 10000
        self.__bankname = "taipei bank"
        self.__rate = 30  # 預設美金與台幣換匯比例
        self.__service_charge = 0.01  # 換匯的服務費

    def save_money(self, money):
        self.__balance += money
        print("存款", money, "complete")

    def get_balance(self):
        print(self.__name.title(), "目前餘額:", self.__balance)

    def usa_to_taiwan(self, usa_d):  # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)  # __cal_rate(usa_d)私有方法
        return self.result

    def __cal_rate(self, usa_d):
        return int(usa_d*self.__rate*(1-self.__service_charge))


hungbank = Banks("hung")
hungbank.get_balance()
hungbank.get_balance()
# 破解私有屬性
# 存取私有屬性 :　物件名稱．＿類別名稱＋私有屬性　相當於　hungbank._Banks__balance
hungbank._Banks__balance = 12000
hungbank.get_balance()
# 破解私有方法 :
hungbank._Banks__cal_rate(50)  # 似破解私有屬性
