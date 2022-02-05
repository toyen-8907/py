# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:00:42 2021

@author: jerry
"""

def kitchen(unserved, served):
    #將未服務的餐點轉為已服務
    print('顧客點的餐點:')
    while unserved:# 如果串列有東西while迴圈就會繼續執行
        current_meal = unserved.pop()
        #模擬出餐過程
        print('菜單:', current_meal)
        #已出餐的加入出餐串列
        served.append(current_meal)

def show_order_meal(unserved):
    '''顯示尚未出餐的餐點'''
    print('=== 下列是尚未服務的餐點 ===')
    if not unserved:
        print('沒有餐點未服務')
    for unserved_meal in unserved:
        print(unserved_meal)

def show_served_meal(served):
    '''顯示已服務的餐點'''
    print('=== 以下是已經服務的餐點 ===')
    if not served:
        print('沒有已服務餐點', '\n')
    for served_meal in served:
        print(served_meal)

ordered = ['fries', 'soda', 'water', 'burger', 'cola', 'sprint']
served = []

#列出餐廳處理前的菜單
show_order_meal(ordered)
show_served_meal(served)

#餐廳服務過程
''' impo************* '''
kitchen(ordered[:], served)        
print('\n', '=== 廚房處理結束 ===', '\n')

show_order_meal(ordered)
show_served_meal(served)



