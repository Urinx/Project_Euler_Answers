#!/usr/bin/env python
#coding:utf-8

"""

Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:
192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""
def is_1_t0_9(s):
	if '0' not in list(s) and len(set(s))==9 and len(s)==9: return True
	return False

def answer():
	m=918273645
	for i in xrange(9000,9999):
		s=str(i)+str(i*2)
		if is_1_t0_9(s):		
			if int(s)>m:
				m=int(s)
	print m

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 932718654
# run time= 0.00355195999146