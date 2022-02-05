# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 16:05:54 2021

@author: jerry
"""
'''
# 最大公約數 
def gcd(n1, n2):
    g = 1
    n = 1
    while n <= n1 and n <= n2:
        if n1 % n == 0 and n2 % n == 0:
            g = n
        n += 1
    return g

n1, n2 = eval(input('請輸入長跟寬兩個整數值'))
print(gcd(n1, n2))
    
# 輾轉相除法

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        tmp = a % b
        
        a = b
        b = tmp
    return a

a, b = eval(input('請輸入兩個整數值'))
print("最大公約數 :", gcd(a,b))

        
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
a, b = eval(input('請輸入兩個整數值'))
print("最大公約數 :", gcd(a,b))
'''

def lcm(a, b):
    f = a * b
    def gcd(a,b):
        if a < b:
            a, b = b, a
        while b != 0:
            tmp = a % b
            a = b
            b = tmp
        return a
    return f/gcd(a, b)
a, b = eval(input('請輸入兩個整數值'))
print(lcm(a, b))