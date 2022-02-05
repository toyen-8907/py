# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:07:57 2021

@author: jerry
"""

grades = [87, 99, 69, 52, 78, 98, 80, 92 ]
grades.sort()
print(grades)
print(max(grades))
print(min(grades))
print(sum(grades))
avg = sum(grades)/len(grades)
print(avg)

old = ['toyota', 'nissan', 'honda']
import copy
old.remove('nissan')
old.insert(1,'ford')
new = copy.deepcopy(old)
print(new)

str1 = '  Python '
str2 = 'is  '
str3 = ' easy'
python = str1.lstrip()
iis = str2.rstrip()
print(python + iis + str3)

city = ['a', 'b', 'c', 'd', 'e']
city.append('london')
print(city)
city.insert(3, 'xian')
city.remove('a')
print(city)

grades1 = [23,2,66,45,69]
grades1.sort()
print(grades1)

grades1.reverse()
print(grades1)
print(max(grades1),min(grades1),sum(grades1))


m = [123]

y = [((x/34)**2) for x in m] #運算式放前面
print(y)

colors = ['red', 'orange', 'gray']
shape = ['square', 'triangle', 'circle']
x = [[shape,colorr] for shape in shape for colorr in colors]
print(x)

sc =[[1,'jy',77,54,100,0,0,0],
     [2,'hg',56,78,95,0,0,0],
     [3,'tu',78,99,88,0,0,0],
     [4,'chen',66,77,88,0,0,0],
     [5,'wang',34,100,56,0,0,0],
     ]
#計算總分與平均
print("請填入總分和平均")
for i in range(len(sc)):
    sc[i][5] = sum (sc[i][2:5])      #填入總分
    sc[i][6] = round((sc[i][5]/3),1) #填入平均
    print(sc[i])
sc.sort(key=lambda x:x[5],reverse = True)
#key=lambda x:x[n] 針對串列內第n個元素值排序的使用方法

print("填入名次")

for i in range(len(sc)):
    sc[i][7]=i+1
for j in range(1,len(sc)):
    if sc[j][5] == sc[j-1][5]:
        for k in range(j,len(sc)):
            sc[k][7]-=1
            print(sc[k])
    
'''
    for j in range(1,len(sc)):
        if sc[j][5] == sc[i][5]:
            sc[j][7] = i
'''


for l in range(1,5):
    
    print(l)






