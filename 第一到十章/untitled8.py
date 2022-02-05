# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:35:56 2021

@author: jerry
"""
'''
soldier0 = {1:0,2:4,3:5}
soldier1 = {1:2,3:34,4:5}
soldier2 = {1:3,2:44,3:32}
armys = [soldier0,soldier1,soldier2]
for army in armys:
    print(army)
'''    
    
armys = []
for soldier in range(20):
    soldier = {'tag': 'red','scores' : 3,'speed': 'slow'}
    armys.append(soldier)

for soldier in armys[:6]:
    print(soldier)
  
print(len(armys))


for soldier in armys[5:8]:
    if soldier['tag'] == 'red':
        soldier['tag'] = 'orange'
        soldier['scores'] = 6
        soldier['speed'] = 'medium'
    print(soldier)
for soldier in armys[:10]:
    print(soldier)
    
    
sports={'curry':['basketball','football'],
       'james':['basketball','soccer'],
       'durant':['basketball'],
       'irving':['badminton']}    
for name,lsport in sports.items():
    print(name)
    for sport in lsport:
        print('     ',sport)
        
        
bodyaccont ={
    'ken':{'birth':'0708','height':192},
    'ben':{'birth':'0301','height':179}
    }
for i,j in bodyaccont.items():
    print(i)
    for k,l in j.items():
        print(k,l)
    
    
seq = (1,2)
list_dict = dict.fromkeys(seq,12)
print(list_dict)
    

value = list_dict.get(1)
print(value)
value = list_dict.setdefault(3,10)
print(list_dict)

a = ['dsd','wdqee']
b = ['dfa','ff','ger']
c = ['wee']
d = {'A':a,'B':b,'C':c}

loc = {(25.0542, 121.5168):'台北車站',
       (22.2838, 114.1731):'宏勘車站'
       }
print(loc)



