# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 14:28:01 2021

@author: jerry
"""

def vip_mem(id, name, tel = ''):
    vip_dict = {'vip_id': id, 'Name' : name}
    if tel:
        vip_dict['Tel'] = tel
    return vip_dict

member = vip_mem('s12093848','陳湯湯')
print(member)
member2 = vip_mem('s12093848','陳湯湯', 12343431)
print(member2)
vip_dictdict = {}
while True:
    id = input('輸入id')
    name = input('輸入名字')
    tel = input('輸入電話')
    member = vip_mem(id,name,tel)
    k = input("繼續執行輸入y反之輸入n")
    vip_dictdict[name] = member
    if k != 'y':
        break
print(vip_dictdict)



def product_msg(costumers):
    str1 = 'dear:'
    str2 = '本公司將在2020舉行產品發布會'
    str3 = '總經理敬上'
    for costumer in costumers:
        msg = str1 + costumer + '\n' + str2 + '\n' + str3
        print(msg)
members = ['ken', 'jer', 'fkek', 'peter', 'rob']
product_msg(members)