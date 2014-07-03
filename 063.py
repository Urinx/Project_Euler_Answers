#!/usr/bin/env python
#coding:utf-8

"""
Powerful digit counts

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
How many n-digit positive integers exist which are also an nth power?

"""
def anwser():
    n_digit=1
    count=0
    while 1:
        for i in xrange(1,10):
            if len(str(i**n_digit))==n_digit:
                count+=1
        if len(str(9**n_digit))<n_digit: break
        n_digit+=1
    print count

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 49
# run time= 0.000367879867554