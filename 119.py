#!/usr/bin/env python
#coding:utf-8

"""
Digit power sum

The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.
We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.
You are given that a2 = 512 and a10 = 614656.
Find a30.

"""
import itertools
import math

def answer():
	a = []
	n = 30
	for b in xrange(2, 600):
		for e in xrange(2, 50):
	 		p = b ** e
			if sum(map(int, str(p))) == b:
				a.append(p)
			if len(a) > n * 1.1:
				break

	a.sort()
	print a[29]

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 248155780267521
# run time= 0.103001117706