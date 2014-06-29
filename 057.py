#!/usr/bin/env python
#coding:utf-8

"""

Square root convergents

It is possible to show that the square root of two can be expressed as an infinite continued fraction.
√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
By expanding this for the first four iterations, we get:
1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

"""
def int_add_fraction(i,f):
	return [f[0]+i*f[1],f[1]]

def expansion(f):
	return int_add_fraction(1,int_add_fraction(1,f)[::-1])

def anwser():
    f=[1,1]
    m=0
    for i in xrange(1,1001):
    	f=expansion(f)
    	if len(str(f[0]))>len(str(f[1])): m+=1
    print m

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 153
# run time= 0.0114748477936