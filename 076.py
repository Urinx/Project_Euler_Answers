#!/usr/bin/env python
#coding:utf-8

"""
Counting summations

It is possible to write five as a sum in exactly six different ways:
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
How many different ways can one hundred be written as a sum of at least two positive integers?

"""

def answer():
    ways=101*[0]
    ways[0]=1
    for i in xrange(1,101):
        for j in xrange(i,101):
            ways[j]+=ways[j-i]
    print ways[-1]-1

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 190569291
# run time= 0.00130701065063
