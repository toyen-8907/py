# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:52:32 2021

@author: jerry
"""

def upper(func):                 #裝飾器 decorator
    def newfunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        print('函數名稱: ' , func.__name__)
        print('函數參數: ' , args)
        return newresult
    return newfunc
def bold(func):
    def wrapper(args):
        return 'bold' + func(args) + 'bold'
    return wrapper

# 裝飾器還有另一常用觀念是為一個函數增加除錯的檢察功能
@upper
@bold
def greeting(string):           # 問候函數
    return string
print(greeting('adsf'))

# mygreeting = upper(greeting)
# print(mygreeting('ggjirjgijadf'))


def errorcheck(func):
    def newfun(*args):
        if args[1] != 0:
            result = func
        else:
            result = '除數不能等於 0'
        print('函數名稱 : ', func.__name__)
        print('函數參數 : ', args)
        print('執行結果 : ', result)
        return result
    return newfun
@errorcheck
def div(x, y):
    return x/y
print(div(1,0))        

# decorator裝飾器可疊加 由下往上執行

