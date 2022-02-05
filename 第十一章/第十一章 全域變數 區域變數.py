# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 18:34:46 2021

@author: jerry
"""

def printmsg():
    #函數本身沒有定義變數，只有執行列印全域變數功能
    print('函數列印', msg) #列印全域變數

mg = 'global variable'    
print('主程式列印', mg)
printmsg()
    
def printmsg():
    #函數本身有定義變數，將執行列印區域變數功能
    msg = 'local variable'
    print('函數列印:', msg)
    print('區域變數',locals())
msg = 'global variable'
print('列印主程式:', msg)
printmsg()


print()



print('全域變數',globals())
  