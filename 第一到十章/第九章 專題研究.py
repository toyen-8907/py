# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:15:23 2021

@author: jerry
"""

lemonade_lyrics = '''Xanny bars, suicide door, brand new bag (ooh-ooh)
College girls give a nigga head in my Rafs (ooh-ooh)
Rockstar life, so much money, it'll make you laugh, hey
These bitches, they hate, and you can't miss what you never had, hey, hey
Off the juice (juice), codeine got me trippin' (juice)
Copped a coupe (coupe), woke up, roof is missin', yeah
Ice (ice), lemonade, my neck was drippin'
Ice (ice), lemonade, my neck was drippin'
Why? (Yеah-yeah-yeah) Why?
Why you wanna waste my timе?
I can tell you really hate your life
Bitch, your watch the same as mine
(Oh, oh, yeah) I can't relate
Designer frames, I'm blind today
(Oh-oh) I'm never late
The money callin', you needed space'''

mydict = {}
songlower = lemonade_lyrics.lower()
print(songlower)

for ch in lemonade_lyrics:
    if ch == ',.?':
        songlower = songlower.replace(ch, ' ')
print(songlower)

songlist = songlower.split()
print(songlist)


for h in songlist:
    if h in mydict:
        mydict[h] += 1
    else:
        mydict[h] = 1
print(mydict)


word = 'djwiwod;rjfrgji'
alphabetcount = {alphabet:word.count(alphabet) for alphabet in word}
print(alphabetcount)










