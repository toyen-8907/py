class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 定義實體方法

    def show(self):
        print(self.x, self.y)

    def distance(self, target_x, target_y):
        return (((self.x - target_x)**2) + ((self.y - target_y)**2))**0.5


p = Point(12, 45)
p.show()  # 呼叫實體方法/函式
print(p.distance(8, 42))

# File 實體物件的設計 : 包裝檔案讀取的程式


class File():
    def __init__(self, name):
        self.name = name
        self.file = None  # 尚未開啟檔案 : 初期是none

    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")

    def read(self):
        return self.file.read()

    def close(self):
        self.file.close()


f1 = File("dada.txt")
f1.open()
data = f1.read()
print(data)
f1.close()
