#!/usr/bin/env python
#coding:utf-8

"""

Double-base palindromes

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)

"""

def anwser():
	s=0
	for i in xrange(1,1000000,2):
		if str(i)==str(i)[::-1]:
			b=str(bin(i))[2:]
			if b==b[::-1]: s+=i
	print s

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 55
# run time= 1.498057127