# ch4_78.py
import pandas as pd
import matplotlib.pyplot as plt

colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv('iris.csv', names = colName)
iris['species'] = iris['species'].apply(lambda x: x.replace("Iris-",""))
# 鳶尾花分組統計均值
iris_mean = iris.groupby('species', as_index=False).mean()
# 繪製堆疊橫條圖
iris_mean.plot(kind='barh',stacked=True)
# 刻度處理
plt.yticks(iris_mean.index,iris_mean['species'], rotation=0)

plt.show()











