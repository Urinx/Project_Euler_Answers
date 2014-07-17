#!/usr/bin/env python
#coding:utf-8

"""
Counting fractions in a range

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that there are 3 fractions between 1/3 and 1/2.
How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

"""
def hcf(a,b):
    if b==0: return a
    return hcf(b,a%b)

def answer():
    m=0
    for b in xrange(5,12001):
        for a in xrange(b/3+1,b/2+b%2):
            if hcf(a,b)==1: m+=1
    print m

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 7295372
# run time= 21.7669148445