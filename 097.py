#!/usr/bin/env python
#coding:utf-8

"""
Large non-Mersenne prime

The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.
However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.
Find the last ten digits of this prime number.

"""
def answer():
	p=1
	for i in xrange(7830457):
		if len(str(p))>11:
			p=int(str(p)[-11:])
		p*=2
	print str(p*28433+1)[-10:]

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 8739992577
# run time= 6.92501306534