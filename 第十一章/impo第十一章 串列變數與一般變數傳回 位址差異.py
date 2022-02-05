# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 19:49:25 2021

@author: jerry
"""

def mydata(n):
    print('函數id(n)=:', id(n), '\t', n)
    n = 5
    print('函數id(n)=:', id(n), '\t', n)

x = 1
print('主程式 id(x) = :', id(x), '\t', x)
mydata(x)
print('主程式 id(x) = :', id(x), '\t', x)

def mydata(n):
    print('函數id(n)=:', id(n), '\t', n)
    n[0] = 5
    print('函數id(n)=:', id(n), '\t', n)
x = [1,2]
print('主程式 id(x) = :', id(x), '\t', x)
mydata(x)
print('主程式 id(x) = :', id(x), '\t', x)