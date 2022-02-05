# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:51:43 2021

@author: jerry
"""

def dsj(asd):
    pass

print(type(abs))




def myrange(start=0, stop=100,step=1):
    n = start
    while n < stop:
        yield n
        n += step
print(type(myrange))
for x in myrange(0,5,1):
    print(x)