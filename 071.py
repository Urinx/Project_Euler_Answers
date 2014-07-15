#!/usr/bin/env python
#coding:utf-8

"""
Ordered fractions

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that 2/5 is the fraction immediately to the left of 3/7.
By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

"""
def f_gt(f1,f2):
    if f1[0]*f2[1]-f1[1]*f2[0]>0: return True
    return False

def hcf(a,b):
    if b==0: return a
    return hcf(b,a%b)

def answer():
    m=[2,5]
    for b in xrange(1000000,5,-1):
        a=3*b/7
        if f_gt([a,b],m) and f_gt([3,7],[a,b]): m=[a,b]
    f=hcf(*m)
    m=[i/f for i in m]
    print m

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# [428570, 999997]
# run time= 0.628713846207