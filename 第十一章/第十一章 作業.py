# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 15:52:14 2021

@author: jerry
"""


'''
def absolute(n):
    if n < 0:
        n = -n
    return n

print(absolute(-11))
'''
'''
def mymax(a,b):
    if a < b:
        return b
    return a

print(mymax(121, 34))

def smallcounter():
    
    n1, n2 = eval(input('輸入欲計算兩數字 : '))
    fun = input('輸入欲用計算方式( add sub mul div) : ',)
    def add(n1, n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2
    def mul(n1, n2):
        return n1 * n2
    def div(n1, n2):
        return n1 / n2
    if fun == 'add':
        return add(n1, n2)
    elif fun == 'sub':
        return sub(n1, n2)
    elif fun == 'mul':
        return mul(n1, n2)
    elif fun == 'div':
        return div(n1, n2)
while True:
    print(smallcounter())
    a = input('若想重複使用城市請輸入 y OR Y :')        
    if a == 'y' or a == 'Y':
        continue
    else:
        break
'''


'''
def cto_F(c):
    return c * (9/5) +32
def fto_C(f):
    return (f-32)*(5/9)
while True:
    a = input('輸入欲轉換成何種溫度系統 c or f (欲結束使用請輸入其他字元):') 
    if a == 'f':
        c = int(input('輸入華氏溫度以轉成攝氏 : '))
        print(cto_F(c))
    elif a == 'c':
        f = int(input('輸入攝氏溫度已轉成華式 : '))
        print(fto_C(f))
    else:        
        break
'''
'''
def pi(i):
    pi = 0
    for a in range(1,i+1):
        b =  4 * (((-1) ** (a+1))/((2*a)-1))
        pi += b
        if a % 1000 == 1:
            print(pi)
    return pi    
print(pi(1))

  
def area(s1, s2, s3):    
    
    p = (s1 + s2 + s3)/2
    areaa = (p*(p-s1)*(p-s2)*(p-s3))**(1/2)
    if (s1 + s2) > s3 and (s1+s3)>s2 and (s2+s3)>s1:
        print('此三邊長可構成一個三角形')
        return areaa
    else:
        return '不是三角形'

print(area(3, 4, 5))

def isPalindrome(s):
    c = str(s)
    a = list(c)
    a.reverse()
    b = []
    for x in a:
        b.append(x)
    a.reverse()
    if a == b:
        return '是回文數字'
    else:
        return '非回文'
print(isPalindrome(22322))    
    



def pizza(size,*toppings):
    print('pizza尺寸為', size,'\n', '配料如下 :')
    for a in toppings:
        print(a)
pizza('12inch', 1,2,3,4,5,6,'g','g','g','g','d','d')

def isPalindrome(a):
    if len(a) <= 1:
        return True
    elif a[0] != a[len(a)-1]:
        return False
    else:
        return isPalindrome(a[1:(len(a)-1)])
ad = input()
if isPalindrome(ad):
    print('yes')
else:
    print('not')
'''    
    
def fib(n):
                        
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print
        return fib(n-1) + fib(n-2)

for index in range(10):
    print("%4d" % fib(index) , end = '')





































