#!/usr/bin/env python
#coding:utf-8

"""

Champernowne's constant

An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

"""

'''
1 9
2 90
3 900
4 9000
5 90000
6 900000
'''

def answer():
	s=''
	a=b=1
	for i in xrange(0,185186):
		s+=str(i)
	while a<=1000000:
		b*=int(s[a])
		a*=10
	print b

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 210
# run time= 0.0683369636536