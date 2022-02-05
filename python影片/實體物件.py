# 實體物件的建立與運用
# 類別兩種用法 1.類別與類別屬性 2.類別與 實體物件、實體屬性
# 要先建立實體物件，才能使用實體屬性

# 實體物件的設計 : 平面座標上的點
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


q = Point(3, 5)
print(q.x, q.y)
w = Point(4, 6)
print(w.x, w.y)

# FULLname 實體物件的設計 :分開紀錄姓、名資料的全名


class FullName:
    def __init__(self, first, last):
        self.first = first
        self.last = last


name1 = FullName("d.y", "chou")
print(name1.first, name1.last)
