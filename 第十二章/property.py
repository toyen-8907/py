class Score:
    def __init__(self, score):
        self.__score = score

    @property
    def sc(self):
        print("inside th getscore ")
        return self.__score

    @sc.setter
    def sc(self, score):
        print("inside the setscore")
        self.__score = score
#    sc = property(getscore, setscore)  # python 風格


stu = Score(213)
print(stu.sc)

print(stu.sc)
# 新式屬性 = property(getter[,setter[,fdel[,doc]]])


stu = Score(0)
print(stu.sc)
stu.sc = 80
print(stu.sc)
# 經裝飾器設計後 未來無法存取私有屬性


class Square():
    def __init__(self, sideLen):
        self.__sideLen = sideLen

    @property
    def area(self):
        return self.__sideLen ** 2


obj = Square(6)
print(obj.area)
