# 封裝變數或函式
# 封裝的變數或函式，統稱類別的屬性

# 定義>>>使用
# 要先定義類別，才能使用類別中封裝的屬性


# 定義類別、與類別屬性(封裝在類別中的變數和函式)
# 定義一個類別IO，有兩個屬性 supportedsrcs & read
class IO:
    supportedsrcs = ["console", "file"]

    def read(src):
        if src not in IO.supportedsrcs:
            print("not supported")
        else:
            print("read from ", src)


# 使用類別
print(IO.supportedsrcs)
IO.read("file")
IO.read("dsdf")
