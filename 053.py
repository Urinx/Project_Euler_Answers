#!/usr/bin/env python
#coding:utf-8

"""

Combinatoric selections

There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, 5C3 = 10.
In general,
C(n,r)=n!/r!(n−r)! ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

"""
from math import factorial as f

def combinator(n,r):
	return f(n)/(f(r)*f(n-r))

def answer():
    m=0
    for n in xrange(23,101):
    	i=0
    	while 1:
    		if combinator(n,n/2-i)<=1000000: break
    		i+=1
    	m+=2*i
    	if n%2==0: m-=1
    print m

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 4075
# run time= 0.0573120117188