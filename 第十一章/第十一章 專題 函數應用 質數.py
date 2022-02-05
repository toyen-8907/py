# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:08:34 2021

@author: jerry
"""

def modifysong(songstr):
    for ch in songstr:
        if ch in '?!,.':
            songstr = songstr.replace(ch,'')
    return songstr
def wordcount(songcount):
    global mydict
    songlist = songcount.split()
    print('以下是歌曲串列 : ', songlist)
    mydict = {wd:songlist.count(wd) for wd in set(songlist)}        



data = '''What you know about rollin' down in the deep?
When your brain goes numb, you can call that mental freeze
When these people talk too much, put that shit in slow motion, yeah
I feel like an astronaut in the ocean, ayy
What you know about rollin' down in the deep?
When your brain goes numb, you can call that mental freeze
When these people talk too much, put that shit in slow motion, yeah
I feel like an astronaut in the ocean'''


mydict = {}
print('以下是將歌曲大寫改成小寫同時將標點符號用空字元改變')
song = modifysong(data.lower())
print(song)

wordcount(song)
print('以下是最後執行結果')
print(mydict)



def isprime(num):
    '''測試是否為質數'''
    for n in range(2,num):
        if num % n == 0:
            return False
    return True
num = int(input('輸入大於一的整數做質數測試'))
if isprime(num):
    print('%d是質數' % num)
else:
    print('%d不是質數' % num)
    
    
    
    
    
    
    
    