#!/usr/bin/env python
#coding:utf-8

'''

Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

'''

a<b<c
a^2+b^2=c^2
a+b+c=1000   ==> a^2+b^2=(1000-a-b)^2  ==> a+b-ab/1000=500
             ==> a<=333 a+b<=666

a=m^2−n^2
b=2mn
c=m^2+n^2

'''

def answer():
	for m in xrange(30,10,-1):
		for n in xrange(m-1,0,-1):
			a=m**2-n**2
			b=2*m*n
			c=m**2+n**2
			if a+b+c==1000:
				print '%d %d %d' % (a,b,c)
				print a*b*c

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
#375 200 425
#31875000