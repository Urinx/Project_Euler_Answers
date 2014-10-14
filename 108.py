#!/usr/bin/env python
#coding:utf-8

"""
Diophantine reciprocals I

In the following equation x, y, and n are positive integers.
1/x+1/y=1/n
For n = 4 there are exactly three distinct solutions:
1/5+1/20=1/4
1/6+1/12=1/4
1/8+1/8=1/4
What is the least value of n for which the number of distinct solutions exceeds one-thousand?
NOTE: This problem is an easier version of Problem 110; it is strongly advised that you solve this one first.

"""
def noDSquared(n,prime):
    nod=1
    remain=n

    for p in prime:
        if p**2>n: return nod*2

        exponent=1
        while remain%p==0:
            exponent+=2
            remain/=p
        nod*=exponent

        if remain==1:
            return nod

    return nod

def answer():
    prime=[2,3,5,7,11,13,17]

    n=1
    limit=1000

    while 1:
        if (noDSquared(n,prime)+1)/2 > limit:
            print n
            break
        n+=1

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 180180
# run time= 0.565303087234