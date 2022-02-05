# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 18:46:41 2021

@author: jerry
"""

fstream1 = open("C:\python\chp4\out1",mode = "w")
print(" 測試輸出 ",file = fstream1)
fstream1.close( )
fstream2 = open("C:\python\chp4\out2",mode = "a")
print("測試追加",file = fstream2)
fstream2.close()
