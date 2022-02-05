# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 16:35:58 2021

@author: jerry
"""
#儲存檔案  讀取檔案
with open("data.txt",mode = "w", encoding=("utf-8"))as file:
    file.write("測試中文")
#讀取檔案
#把檔案中的數字資料，一行一行的讀取出來，並計算總合
sum = 0
with open("data.txt",mode ="r", encoding=("utf-8")) as file:
    for line in file:
       sum += int(line) 
print(sum)