# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:01:10 2021

@author: jerry
"""

abc = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
encry_dict = {}
front3 = abc[:3]
end = abc[3:]
subtext = end + front3 

encry_dict = dict(zip(subtext,abc))
print(encry_dict)
