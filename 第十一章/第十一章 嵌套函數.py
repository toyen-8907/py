# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 12:27:46 2021

@author: jerry
"""

def dist(x1,x2,y1,y2):
    def mysqrt(z):
        return z ** 0.5
    dx = (x1 - x2) ** 2
    dy = (y1 - y2) ** 2
    return mysqrt(dx+dy)
print(dist(1, 4, 2, 6))


def outer():
    def inner(n):
        print('inner running')
        return sum(range(n))
    return inner

f = outer()
print(f)
print(f(5))

y = outer()
print(y)
print(y(11))


#閉包 閉包內的數值不會被未來的變數宣告更改
def outer():
    b = 10
    def inner(x):
        return 5 * x + b
    return inner
b = 2
f = outer()
print(f(b))


