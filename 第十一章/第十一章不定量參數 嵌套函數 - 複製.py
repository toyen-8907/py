# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:10:30 2021

@author: jerry
"""
'''
def make_icecream(ice_type = '清冰',*toppings):
    # 零到多用* *可將傳遞參數化為元祖
    print('%s配料如下' % ice_type)
    for topping in toppings:
        print('----',topping)
    print(type(toppings))
    print(toppings)
make_icecream('fjidf','df','df','f','we','t','qwet','th','r','th')
make_icecream()

def build_dict(name, age, **players):
    #建立球員資料
    info = {}
    info['name'] = name
    info['age'] = age
    for key,value in players.items():
        info[key] = value
    return info #回傳所建立字典
player_dic = build_dict('df', 23, city = 'okc',country = 'usa')
print(player_dic)

dd = []
player_dic = {}
for player_dicT in range(1,11):
    player_dic[player_dicT] = build_dict(player_dicT, 23, city = player_dicT,country = player_dicT)
    dd.append(player_dic[player_dicT])
    
print(player_dic)
print(dd)
'''

def greeting(name):
    '''函數需傳遞名字'''
    print(name)
help(greeting)
print(greeting.__doc__)
gr = greeting
print(gr)
gr('kkg')
   