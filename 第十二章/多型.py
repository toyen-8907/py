
class Animals():
    """animals類別，這是基底類別"""

    def __init__(self, animal_name):
        self.name = animal_name

    def which(self):
        return "my pet" + self.name.title()

    def action(self):
        return "sleeping"


class Dogs(Animals):
    """dogs類別，是animals的衍生類別"""

    def __init__(self, dog_name):
        super().__init__(dog_name.title())

    def action(self):
        return "running in the street"


class Monkey():
    "猴子類別，這是其他類別"

    def __init__(self, monkey):
        self.name = "My monkey" + monkey.title()

    def which(self):        # 回傳動物名稱
        return self.name

    def action(self):
        return "running in the street"


def doing(obj):                 # 列出動物的行為
    print(obj.which(), "is", obj.action())


my_cat = Animals("sb")  # animals物件
doing(my_cat)
my_dog = Dogs("jeoo")
doing(my_dog)
my_monkey = Monkey("pi")
doing(my_monkey)

# 多重繼承


class Grandfather():
    '''定義祖父類別'''

    def action1(self):
        print("grandfather")


class Father(Grandfather):
    '''定義父親類別'''

    def action3(self):
        print("father")


class Uncle(Grandfather):
    '''定義叔父類別'''

    def action2(self):
        print("uncle")


class Ivan(Father, Uncle):
    '''定義 IVAN 類別'''

    def action4(self):
        print("Ivan")


ivan = Ivan()
ivan.action4()
ivan.action3()
ivan.action2()
ivan.action1()

# super應用在多重繼承的問題


class A():
    def __init__(self):
        super().__init__()
        print("class A")


class B():
    def __init__(self):
        super().__init__()
        print("B")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("class c")


x = C()
