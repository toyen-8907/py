# ch4_42.py
import pandas as pd

course = ['Chinese', 'English', 'Math', 'Natural', 'Society']
chinese = [14, 12, 13, 10, 13]
eng = [13, 14, 11, 10, 15]
math = [15, 9, 12, 8, 15]
nature = [15, 10, 13, 10, 15]
social = [12, 11, 14, 9, 14]

df = pd.DataFrame([chinese, eng, math, nature, social],
                  columns = course,
                  index = range(1,6))
total = [df.iloc[i].sum() for i in range(0, 5)]
df['Total'] = total
print(df)









