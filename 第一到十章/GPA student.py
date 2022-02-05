# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 21:28:44 2020

@author: jerry
"""
count=0
while count != 2 :
    count+=1

    s=['國文','數學','英文','理化']
    L=[]
    name=input('請輸入名字')
    
    loop=0
    while loop != len(s):
        try:
            score=int(input('輸入%s成績: '%s[loop]))
            L.append(score)
            loop+=1
        except ValueError:
            print('Please enter correct number!')
   
    print('-'*20)
    print('第%d位學生'%count)
    print('x'*20)

    print("姓名:",name)


    for i,j in zip(L,s):
            gpa=0
            rank=''
            if 90 <= int(i) <= 100:
                gpa = 4.3
                rank = 'A+'
                
                
            elif 85<= int(i) <=89:
                gpa = 4
                rank = 'A'    
        
            elif 80<= int(i) <=84:
                gpa = 3.7
                rank = 'A-'
        
            elif 77 <= int(i) <= 79:
                gpa = 3.3
                rank = 'B+'
        
            elif 73 <= int(i) <= 76:
                gpa = 3
                rank = 'B'
        
            elif 70 <= int(i) <= 72:
                gpa = 2.7
                rank = 'B-'
    
            elif 67 <= int(i) <= 69:
                gpa = 2.3
                rank = 'C+'
    
            elif 63 <= int(i) <= 66:
                gpa = 2
                rank = 'C'
    
            elif 60 <= int(i) <= 62:
                gpa = 1.7
                rank = 'C-'
    
            elif 0 <= i <= 59:
                gpa = 0
                rank = 'F'

    
            print('%s GPA: %f/%s'%(j,round(gpa,2),rank))    
    print('x'*20)
    
    
    
    
    
    
    