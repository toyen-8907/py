# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:07:57 2021

@author: jerry
"""
'''
grades = [87, 99, 69, 52, 78, 98, 80, 92 ]
grades.sort()
print(grades)
print(max(grades))
print(min(grades))
print(sum(grades))
avg = sum(grades)/len(grades)
print(avg)

old = ['toyota', 'nissan', 'honda']
import copy
old.remove('nissan')
old.insert(1,'ford')
new = copy.deepcopy(old)
print(new)

str1 = '  Python '
str2 = 'is  '
str3 = ' easy'
python = str1.lstrip()
iis = str2.rstrip()
print(python + iis + str3)

city = ['a', 'b', 'c', 'd', 'e']
city.append('london')
print(city)
city.insert(3, 'xian')
city.remove('a')
print(city)

grades1 = [23,2,66,45,69]
grades1.sort()
print(grades1)

grades1.reverse()
print(grades1)
print(max(grades1),min(grades1),sum(grades1))


m = [123]

y = [((x/34)**2) for x in m] #運算式放前面
print(y)

colors = ['red', 'orange', 'gray']
shapes = ['square', 'triangle', 'circle']
x = [[shape,colorr] for shape in shapes for colorr in colors]
print(x)


scores = [33, 23, 44, 11, 43, 17, 22, 50, 30]
game = 0
for score in scores:
    if score <30:
        continue
    game += 1
    
print("有%d場得分超過30分"% game)


scores.sort(reverse = True)
count = 0
for score in scores:
    count += 1
    print(score,end = " ")
    if count ==5:
        break
    


num = int(input("請輸入大於一的整數做質數測試"))
if num == 2:
    print("%d是質數" % num)
else:
    for n in range(2,num):
        if num % n == 0:
            print("%d不是質數" % num)
            break
    else:
        print("%d是質數" % num)
'''

'''
msg1 = 'lets chat'
msg2 = '輸入end為結束聊天'

msg = msg1 + '\n' + msg2 + '\n' + '\\' + '='
input_msg = ''



while input_msg != 'end':
    input_msg = input(msg)
    if input_msg != 'end':
        print(input_msg)

#
active = True
while active:
    input_msg = input(msg)
    if input_msg != 'end':
        print(input_msg)
    else:
        active = False
        
        
# while要有結束條件才會結束迴圈  false時結束

answer = input("請輸入 1-100 數字")
answer = int(answer)
guess = 0
while guess != answer:
    guess = int(input("猜 1-100 數字"))
    if guess > answer:
        print("猜小一點")
    elif guess < answer:
        print("猜大一點")
    else:
        print("right answer")
'''



# 哨兵值 設定一個讓迴圈結束的數值
'''
n = int(input("請輸入一個值"))
sum = 0
while n != 0:
    sum += n
    n = int(input("請輸入一個值"))
print("輸入總和 = ", sum)
'''

'''
tuition = 40000
year = 0
while tuition < 60000:
    tuition = int(tuition * 1.05)
    year += 1
    print(tuition)
print("%d年後學費為%s" % (year,tuition))


for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print(i,'*',j,'=',result)
    print()#換行輸出




i = 1
while i <= 9:
    j = 1
    while j <= 9:
        ans = i * j
        
        print("%d * %d = %s" %(i,j,ans))
        j += 1
    print()
    i += 1
'''

msg = "輸入"
'''
while True:
   input_msg = input(msg)
   if input_msg == "q":
       break
   else:
       print(input_msg)
'''      
'''      
#7_37
PLAYERS = ['a', 'b', 'c', 'd','e']
n = int(input("請輸入人數 ="))
if n > len(PLAYERS): n = len(PLAYERS)
index = 0
while index <= len(PLAYERS):
    if index == n:
        break
    print(PLAYERS[index], end='\n' )
    index +=1




#7_38
index = 0
while index <= 10:
    index += 1
    if(index % 2 !=0):
        continue
    print(index)



asss = ['2', '3', '4', '5', '7', '12', '34', '2']
a = input("請輸入玉刪除數字")
print("before")
while a in asss:
    asss.remove(a)
print(asss)
'''
#7_40******important
'''
buyers = [['jason',1000],
          ['kate',300],
          ['leo',3000],
          ['alice',111],
          ['hank',560]]
goldbuyers = []
vipbuyers = []
while buyers: #執行買家分類迴圈，分類完成迴圈才會結束
    index_buyer = buyers.pop()
    if index_buyer[1] >= 565:
        vipbuyers.append(index_buyer)
    else:
        goldbuyers.append(index_buyer)
print("vipbuyers", vipbuyers)        
print("goldbuyers", goldbuyers)
print(buyers)

#while True:是無限迴圈的方法 true可改成1 還未完成的迴圈可以用pass來處理 7_41

# 解析enumerate
ab = ['c','b','h']
#建立enumerate物件
for a in enumerate(ab):
    print(a)
for count,b in enumerate(ab):
    print(count,b)
print("--------------------------------------------")
#建立enumerate物件
for c in enumerate(ab,4):
    print(c)
for count,d in enumerate(ab,4):
    print(count,d)

#7_43
scores = [23,34,3,56,24,12,76,34]
#不使用enumerate物件
index = 1
for score in scores:
    if score >= 20:
        print("場次%d : 得分%d" %(index, score))
    index += 1


#7_44
for count,i in enumerate(scores,1):
    if i >= 20:
        print(count,i)
    count += 1

products = ['電視','電腦','手機','ps4','switch']
list1 = []
print("j購物平台")
print(products,"\n")
while 1:
    pro = input("輸入欲買商品(q為結束購物):")
    if pro == 'q':
        break
    else:
        if pro in products:
            list1.append(pro)
            products.remove(pro)
print(products)
print(list1)            
'''

#7_46
sc =[[1,'jy',77,54,100,0,0,0],
     [2,'hg',56,78,95,0,0,0],
     [3,'tu',78,99,88,0,0,0],
     [4,'chen',66,77,88,0,0,0],
     [5,'wang',34,100,56,0,0,0],
     ]
#計算總分與平均
print("請填入總分和平均")
for i in range(len(sc)):
    sc[i][5] = sum (sc[i][2:5])      #填入總分
    sc[i][6] = round((sc[i][5]/3),1) #填入平均
    print(sc[i])
sc.sort(key=lambda x:x[5],reverse = True)
#key=lambda x:x[n] 針對串列內第n個元素值排序的使用方法
    
print("填入名次")

for i in range(len(sc)):
    if i == 0:
        sc[i][7] = 1
    else:   
        if sc[i][5] == sc[i-1][5]:
            sc[i][7] = sc[i-1][7]
        else:
            sc[i][7] = i+1
    print(sc[i])

    
 
'''
#以下座位排序
sc.sort(key=lambda x:x[0])
print("最後成績單名次")
for i in range(len(sc)):
    print(sc[i])
'''         
'''        
for j in range(1,len(sc)):
        if sc[j][5] == sc[i][5]:
            sc[j][7] = i




    for j in range(1,len(sc)):
        if sc[j][5] == sc[i][5]:
            sc[j][7] = i
'''
'''

x = 1000001
pi = 0
for i in range(1,x+1):
    pi += 4*((-1)**(i+1)/(2*i-1))
    if i != 1 and i % 100000 == 0:
        print("當 i = %d時 pi = %20.19f" % (i,pi))

'''






