# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 18:08:13 2021

@author: jerry
"""

def mutifunction(x1, x2):
    addresult = x1 + x2
    subresult = x1 - x2
    mulresult = x1 * x2
    divresult = x1 / x2
    return addresult, subresult, mulresult, divresult
x1 = x2 = 120
ans = mutifunction(x1, x2)
print(ans[0])
print(ans[1])
print(ans[2])
print(ans[3])

















