# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 16:49:28 2021

@author: jerry
"""
# recrusive
# 每次呼叫自己時，都會使範圍越來越小
# 必須要有一個終止條件來結束遞迴函數 
# 最大遞迴次數1000次

def factorial(n):
    if n == 1:
        return 1
    else:
        return (n*factorial(n-1))

value = 5
print(value,'的街乘 = ', factorial(value))
