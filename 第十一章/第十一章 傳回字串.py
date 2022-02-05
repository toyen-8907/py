# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 14:17:52 2021

@author: jerry
"""

def info(firstname, lastname, gender, middlename = ''):
    if gender == 'M' or gender == 'm':
        welcome = lastname + middlename + firstname + '先生歡迎你'
    else:
        welcome = lastname + middlename + firstname + '小姐歡迎你'
    return welcome

info1 = info('sheng', 'fan ', 'm')
print(info1)