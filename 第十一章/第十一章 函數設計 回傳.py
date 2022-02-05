# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 18:16:50 2021

@author: jerry
"""

def subtract(x1,x2):
    return x1 - x2
def addition(x1,x2):
    return x1 + x2
#值要回傳
'''
print('subtract or addition ')
print('1:subtract\n','2:addition' )
op = int(input('1 or 2:'))
a = int(input('num:'))
b = int(input('num:'))
'''
#程式運算
while True:
    print('subtract or addition ')
    print('1:subtract\n','2:addition' )
    op = int(input('1 or 2:'))
    a = int(input('num:'))
    b = int(input('num:'))
    if op == 1:
        print('a - b =',subtract(a, b))
        break
    elif op == 2:
        print('a + b = ',addition(a, b))
        break
    else:
        print('error')
        continue