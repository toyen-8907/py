# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:53:23 2021

@author: jerry
"""

def total(data):
    return sum(data)

x = [1, 45, 656]
mylist = [min, max, sum, total]
for f in mylist:
    print(f,f(x))
    
    
def add(x, y):
    return x+y
def mul(x, y):
    return x*y
def running(func, arg1, arg2):
    return func(arg1, arg2)
result1 = running(add, 123, 23)
print(result1)
result2 = running(mul, 112, 345)
print(result2)    
    
def mysum(*args):
    return sum(args)
def run_with_mul_arg(func, *args):
    return func(*args)

print(run_with_mul_arg(mysum, 1, 45, 56, 432, 14))



