# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:24:14 2020

@author: jerry
"""
#除錯
#LIST.append() 可在list裡面加東西
nop=int(input('people in class?'))
count=0
classl=[]
while count != nop :
    count += 1    
    #range(nop)
    s=['國文','數學','英文','理化']
    L=[]
    name=input('請輸入名字:')
    L.append(name)
     
    '''nloop=0
    while nloop != nop :
        nloop += 1    
        #range(nop)
        s=['國文','數學','英文','理化']
        L=[]
        name=input('請輸入名字:')
        #p=[(name(range(nloop)))]
    '''   
    
    average=0
    scorel=[]
    loop=0
    while loop != len(s):
        try:
            score=int(input('輸入%s成績: '%s[loop]))
            scorel.append(score)
            average+=scorel[loop]
            loop+=1
            if loop == len(s):
                average/=4
                scorel.append(round(average,2))
        except ValueError:
            print('Please enter correct number!')  
    
    #average = (scorel[0]+ scorel[1]+scorel[2]+scorel[3])/4              
    L.append(scorel)
    
    
    gradel=[]
    gpal=[]
    rankl=[]
    for i in (scorel):
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
            
        gpal.append(round(gpa,2))
        rankl.append(rank)
    L.append(gpal)
    L.append(rankl)

    classl.append(L)
  
    
s.append('平均')
for l in range(nop):
    print('名字:',classl[l][0])
    for i,j,k in zip(s,classl[l][2],classl[l][3]):        

        print('%s gpa/rank:%f / %s'%(i,j,k))
'''
gpatranslate(90)
def gpatranslate(score):
    