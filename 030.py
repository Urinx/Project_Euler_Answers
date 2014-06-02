#!/usr/bin/env python
#coding:utf-8

"""

Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""

'''
Because
	6*9^5=354294
	7*9^5=413343
Also
	3^5+5*9^5=295488
	2^5+5*9^5=295277
Thus thhe digit is less than or equal to 6.
'''
def anwser():
	a=[]
	for i in xrange(10,295277):
		m=sum([int(j)**5 for j in list(str(i))])
		if i==m: a.append(i)
	print sum(a)

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 443839
# run time= 1.42608499527