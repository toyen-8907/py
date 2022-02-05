# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:03:52 2021

@author: jerry
"""

"""
x, y = eval(input("enter two numbers"))
max_ =x if x > y else y
"""
'''

A = [12, 34, 34, 55]
B = A[:] #切片拷貝新串列:位址不同
print(A)
print(B)
B.append('d')
print(B)


str1 = "D:\python\ch6"
slist = str1.split("\\")
print(slist)
print('\\t')
print(r'\'')




path = ['D:', 'python', 'ch6']
connect = '\\'
print(connect.join(path))
connect='&*&*'
print(connect.join(path))


sports = ['basketball', 'soccer', 'tennis', 'football']
sport = input("請輸入欲增加之運動科目")
if sport in sports:
    print("已在科目中")
else:
    sports.append(sport)
    print(sports)



x = []
if x is None:
    print("x is none")
else:
    print("x isnt none")
'''
#增加串列索引值
'''
drinks = ['cola', 'juice', 'wine']
enumerate_drink = enumerate(drinks)
enumerate_drink2 = enumerate(drinks, start = 5)
print(enumerate_drink)
print(type(enumerate_drink))


print(list(enumerate_drink))
print(list(enumerate_drink2))

#製作大型串列資料
asia = ['bejing','tokyo','taipei','hong kong']
usa = ['chicago','new york','los angeles']
europe = ['paris','london','amsterdam']
world = [asia, usa, europe]
print(world)


#使用者帳號管理系統
accounts = []
account = input("請輸入新帳號 =")
accounts.append(account)

print("公司系統")
ac = input("ENTER ACCOUNT:")
if ac in accounts:
    print("歡迎登入")
else:
    print("帳號不存在")
'''
#文件加密
abc = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
print(subText)










































