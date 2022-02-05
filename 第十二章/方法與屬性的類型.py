class Counter():
    counter = 0  # 類別屬性，可由類別本身調用

    def __init__(self):
        Counter.counter += 1  # 更新指標

    @classmethod
    def show_counter(cls):  # (類別方法)，可由類別本身調用
        print("class method")
        print("counter = ", cls.counter)  # 也可使用 Counter.counter 調用
        print("counter = ", Counter.counter)


one = Counter()
two = Counter()

Counter.show_counter()


# 靜態方法 >>> 類別名稱直接調用
class Pizza():
    @staticmethod
    def demo():
        print("i like pizza")


Pizza.demo()
