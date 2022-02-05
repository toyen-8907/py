# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 21:20:38 2021

@author: jerry
"""

abc = 'abcdefghijklmnopqrstuvwxyz'
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subtext = end23 + front3 

encry_dict = dict(zip(subtext,abc))
print(encry_dict)

m = 'apple'
cipher = []
for i in m:
    i = encry_dict[i]
    cipher.append(i)
print(cipher)
ciphertext = ''.join(cipher)
print(m,'\n',ciphertext)


address_dict = {'chou':'台中',
           'jay':'台北'}

for name,address in address_dict.items():
    print(name,':',address)
print()
message = '1:新增 2:編輯 3:刪除 4:結束\n'

while True:
    selection = input(message)
    if selection == '1':
        name = input()
        address = input()
        address_dict[name] = address
    elif selection == '2':
        while True:
            name = input()
            if name not in address_dict:
                print('error')
            else:
                address = input()
                address_dict[name] = address
                break   #離開迴圈
    elif selection == '3':
        while True:
            name = input()
            if name not in address_dict:
                print('error')
            else:
                del address_dict[name]
                break
    else:
        print('end')
        break
print('new')
for name, address in address_dict.items():
    print(name,':',address)
        
