#!/usr/bin/env python
#coding:utf-8

"""
Odd period square roots

All square roots are periodic when written as continued fractions and can be written in the form:

For example, let us consider √23:

If we continue we would get the following expansion:

The process can be summarised as follows:

It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.
The first ten continued fraction representations of (irrational) square roots are:
√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5
Exactly four continued fractions, for N ≤ 13, have an odd period.
How many continued fractions for N ≤ 10000 have an odd period?

"""
import math

def sqrt_Continued_Fractions(num):
    a0=int(math.sqrt(num))
    r=[[0,1,a0]]
    while 1:
        p=r[-1][2]*r[-1][1]-r[-1][0]
        q=(num-p**2)/r[-1][1]
        a=(a0+p)/q
        if [p,q,a] in r:
            k=len(r)-r.index([p,q,a])
            break
        r.append([p,q,a])
    return [[i[2] for i in r],k]

def anwser():
	a=0
	b=set(range(2,10000)) ^ set([i**2 for i in xrange(2,100)])
	for N in b:
		if sqrt_Continued_Fractions(N)[1]%2!=0: a+=1
	print a

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 1322
# run time= 0.478819131851