# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 16:41:27 2021

@author: jerry
"""

dic = {1:12,'樓層' :'b6',}
dic['tf'] = 1111
dic1 ={1:33,'de':20}

'''
soldier0 = {'tag':'blue','score':5,'blood':10,'xposi': 23,'yposi':11,'speed':'slow'}
print('x=',soldier0['xposi'],'y=',soldier0['yposi']) 
if soldier0['speed'] == 'slow':
    x_move = 8
elif soldier0['speed'] == 'medium' :
    x_move = 23
else:
    x_move = 28
soldier0['xposi'] += x_move
print('new x=',soldier0['xposi'])
'''

# del name_dict[key] 可刪除特定鍵的元素
# value = dic.pop(key[])
print(dic)
value = dic.pop('樓層')
print(dic)

b = dic.copy()

import copy
c = copy.deepcopy(dic)
dic['tf']=0

print(dic ,b ,c)
print(len(c),len(dic))

# in name_dict 可厭證鍵元素是否存在
'''
key = input('輸入鍵:')
value = input('樹入值:')
if key in dic:
    print('已在')
else:
    dic[key] = value
    print("new dic:",dic)
'''

# update() 合併字典

dic.update(dic1)
print(dic)


for i in dic1:
    print(i)
    print(i,dic[i])
#.key()取鍵 
#.value()取值
# in set(xxx.value()) 取值不重複

diclst = sorted(dic.items(),key = lambda item:item[1])
print(diclst)








