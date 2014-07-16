#!/usr/bin/env python
#coding:utf-8

"""
Counting fractions

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that there are 21 elements in this set.
How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

"""
def P(L):
    phi = range(L+1)
    for n in xrange(2, L+1):
        if phi[n] == n:
            for k in xrange(n, L+1, n):
                phi[k] = phi[k] / n * (n-1)
    return sum(phi) - 1

import time
tStart=time.time()
print P(1000000)
print 'run time=',time.time()-tStart
# 303963552391
# run time= 0.937504053116