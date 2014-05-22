#!/usr/bin/env python
#coding:utf-8

"""

Names scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K 
text file containing over five-thousand first names, begin by 
sorting it into alphabetical order. Then working out the alphabetical 
value for each name, multiply this value by its alphabetical position 
in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the 
list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

def anwser():
    total=0
    f=open('names.txt')
    names=f.read().replace('"','').split(',')
    f.close()
    names.sort()
    for i in xrange(0,len(names)):
        total+=(i+1)*sum(map(lambda x:ord(x)-64,list(names[i])))
    print total

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 871198282
# run time= 0.0195789337158