# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:27:10 2021

@author: jerry
"""
#儲存檔案
#import os
'''
with open("da.txt",mode = "w", encoding=("utf-8"))as file:
    file.write("測試中文")
'''
# save_path = '/desktop'
# file_name = "da.txt"
# completeName = os.path.join(save_path, file_name)
# print(completeName)    

# file = open("dat.txt",mode="w",encoding=("utf-8"))
# file.write("嗨嗨嗨嗨")
# file.close()

# 使用json格式讀取、複寫檔案
import json
# 從檔案中讀取json資料,放入變數data裡面
with open("config.json",mode="r",encoding=("utf-8"))as file:
    data = json.load(file)
print(data) # data是字典資料
print("name:",data["name"])
print("version:",data["version"])
data["name"] = 123 #修改變數中的資料
# 把最新的資料複寫回檔案中
with open("config.json",mode="w",encoding=("utf-8"))as file:
    json.dump(data,file)





