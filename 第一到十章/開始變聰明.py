# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#1 123
#2 1230
#3 num1num2
#4 num1+num2
#5 123
#6 num1+num2
#7 str(num1+num2)
x='123+123'
l=[1,3,2,]
美金 = ""
while 美金 != "使用完畢":
    美金 = input("美元")
    if 美金 != "使用完畢":
        台幣 = (float(美金)*30.5)
        #print("新台幣"+str(台幣)+"元") 
        print('新台幣 %f 元\n美金為 %s'%(台幣,美金)) 

    elif 美金 == "使用完畢":
        print('Thank you! %s'%美金)
    else:
        print('Please enter correct number!')


for i in l:
    for j in l:
        print(i+j)
