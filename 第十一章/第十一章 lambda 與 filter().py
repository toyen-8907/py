# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:53:30 2021

@author: jerry
"""
#lambda 匿名函數 只能用一行表達式
square = lambda x:x**2
print(square(4))


'''
product = lambda x, y: x*y
print(product(12, 3))


def func(b):
    return lambda x: 2*x+b
d = func(1)
print(d(12))
f = func(2)
print(f(13))

def mycar(cars,func):
    for car in cars:
        print(func(car))
def wdcar(carbrand):
    return 'my dream car is ' + carbrand.title()
dreamcars = ['porsche','rolls royce','maserati']
mycar(dreamcars, wdcar)
print
'''
def mycar(cars,func):
    for car in cars:
        print(func(car))

dreamcars = ['porsche','rolls royce','maserati']
mycar(dreamcars, lambda carbrand:'my dream car is'+ carbrand.title())



# filter() 篩選序列 filter(func,iterable) 
# 將func函數執行結果回傳是true的元素組成新的篩選物件傳回
'''
def oddfn(x):
    return x if (x % 2 == 1) else None
'''
mylist = [2, 54, 6, 4, 123, 45, 11, 23]
#filter_fadf = filter(oddfn, mylist) #是篩選物件非串列
# filter函數只能被取走一次
'''
print('奇數串列 :',[item for item in filter_fadf])
'''
oddlist = list(filter(lambda x : (x % 2 == 1), mylist)) #filter過濾器
print(oddlist) 

for i in filter(lambda x : (x // 2 >= 12), mylist):
    print(i)
    
    # map(func,iterable) 
for p in map(lambda x : x*2, mylist): #全部賦值
    print(p)
a = list(map(lambda x : x*2, mylist))
print(a)


x = map(lambda x : x-1, mylist)
for f in x:
    print(f)

# reduce(func,iterable) 
# func必須有兩個參數




from functools import reduce
def strtoint(s):
    # def chartonum:
        #return {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    #return reduce(lambda x,y : 10*x+y,map(chartonum,s))
    def func(x,y):
        print('a')
        return 10*x+y
    def charToNum(s):
        print('s = ', type(s), s)
        mydict = {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        n = mydict[s]
        print('n = ', type(n), n)
        return n
        print(map(charToNum, s))
        #k = list(map(charToNum, s))    
    return reduce(func, map(charToNum, s))



string = '999'
x = strtoint(string) + 10
print('x = ', x)

w = '700000000000000000000000000000000000000000000000000000000000000000000000000000'
print(int(w))

print(2**16)



