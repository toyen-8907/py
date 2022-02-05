# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:40:04 2021

@author: jerry
"""

cd = {'ert', 'gh', 'asjdf'}
dc = {'ert', 'ewqq', 'erww', 'fef'}
both = cd & dc
print(both)

alll = cd | dc
print(alll)


asd = cd - dc
ac = cd.difference(dc)
print(asd,'\n',ac)  


aw = cd ^ dc
print(aw)

s = aw
s.add('21344')
print(aw,s)

shallow = s.copy()
shallow.add(12313132)
print(s,'\n',shallow)

