#!/usr/bin/env python
#coding:utf-8

"""

Digit canceling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""

'''
ab/bc=a/c
b=[2-9]
a<b
'''

def anwser():
	denominator=numerator=1
	for b in xrange(2,10):
		for a in xrange(1,b):
			for c in xrange(1,10):
				m1=(10*a+b)/float(10*b+c)
				m2=a/float(c)
				if m1==m2:
					numerator*=a
					denominator*=c
	print denominator/numerator

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 100
# run time= 0.0003981590271