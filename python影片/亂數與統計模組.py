
import statistics as stat
import random
'''
# 從列表中隨機選取一個資料
random.choice([1, 3, 5, 6, 7])
# 從列表中隨機選取兩個資料
random.sample([1, 3, 4], 2)
# 將列表的資料[就地]隨機調換順序
data = [0, 4, 78, 421]
random.shuffle(data)
print(data)
# 隨機亂數 取得0.0~1.0之間的隨機亂數
random.random(0.0, 1.0)
# 常態亂數分配 取得平均數100,標準差10的 # 常態分配亂數
random.normalvariate(100, 10)
# 統計模組
# 計算列表中數字的平均值
statistics.mean([1, 4, 67, 8])
# 中位數
statistics.median([1, 4, 56, 66, 43])
# 標準差
statistics.stdev([1, 4, 6])
'''


data = random.sample([1, 3, 5, 6, 7, 8, 9, 0, 4134, 34], 3)
print(data)
data = [1, 3, 56, 89, 134]
random.shuffle(data)
print(data)

data = random.random()  # 0.0 到 1,0 之間隨機亂數
print(data)
data = random.uniform(0.0, 1.0)  # 0.0 到 1,0 之間隨機亂數 = random.random
print(data)

data = random.normalvariate(100, 10)
print(data, '\n')
data = stat.median([1, 4, 56, 66, 43])
print(data)
data = stat.mean([1, 4, 6, 34, 7, 8, 78])
print(data)
data = stat.stdev([1, 4, 6])
print(data)
