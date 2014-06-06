#!/usr/bin/env python
#coding:utf-8

"""

Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""
import math

def anwser():
	m=0
	for i in xrange(10,2540160):
		if i==sum([math.factorial(int(j)) for j in list(str(i))]): m+=i
	print m

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 40730
# run time= 14.8498859406