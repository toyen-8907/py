# ex12_7.py
class Father():
    """ 定義父親的資產 """
    def __init__(self):
        self.fathermoney = 10000
   
class Ira(Father):                                  # 父類別是Father
    """ 定義Ira的資產 """
    def __init__(self):
        self.iramoney = 8000
        super().__init__()
    def get_money(self):                            # 取得資產明細
        print("Ira資產: ", self.iramoney,
              "\n父親資產: ", self.fathermoney,
              "\nIvan資產 : ", Ivan().ivanmoney)    # 注意寫法   
   
class Ivan(Father):                                 # 父類別是Father
    """ 定義Ivan的資產 """
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()   
    def get_money(self):                            # 取得資產明細
        print("Ivan資產: ", self.ivanmoney,
              "\n父親資產: ", self.fathermoney,
              "\nIra資產 : ", Ira().iramoney)       # 注意寫法

ira = Ira()
ira.get_money()                                     # 取得資產明細

