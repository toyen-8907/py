
class Person():
    def job(self):
        print("hello")


class LawerPerson(Person):
    def job(self):
        print("你好")


hung = Person()
han = LawerPerson()
hung.job()
han.job()

# 衍生類別引用基底類別的方法 super()


class Animals():
    """animals類別，這是基底類別"""

    def __init__(self, animal_name, animal_age):
        self.name = animal_name
        self.age = animal_age

    def run(self):
        print(self.name.title(), "is running")


class Dogs(Animals):
    """dogs類別，是animals的衍生類別"""

    def __init__(self, dog_name, dog_age):
        super().__init__("my pet " + dog_name.title(), dog_age)

    def sleeping(self):
        print("my pet", "is sleeping")


mycat = Animals("kattie", 3)
print(mycat.name.title(), "is", mycat.age, "years old.")
mycat.run()

mydog = Dogs("jojo", 2)
print(mydog.name.title(), "is", mydog.age, "years old")
mydog.run()
mydog.sleeping()

# 三代同堂的類別與取得基底類別的屬性super() 父屬性與子屬性都須super().__init__


class Grandfather():
    # 定義父親的資產
    def __init__(self):
        self.grandfathermoney = 10000

    def get_info1(self):
        print("father's information")


class Father(Grandfather):
    # 定義ira的資產
    def __init__(self):
        self.iramoney = 8000
        super().__init__()

    def get_info2(self):
        print("father's information")


class Ivan(Father):
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()

    def get_info3(self):
        print("ivan's information")

    def get_money(self):
        print("\nivan資產 : ", self.ivanmoney,
              "\n父親資產 : ", self.iramoney,
              "\n祖父資產 : ", self.grandfathermoney)


ivan = Ivan()
ivan.get_info3()
ivan.get_info2()
ivan.get_info1()
ivan.get_money()
