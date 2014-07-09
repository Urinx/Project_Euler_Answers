#!/usr/bin/env python
#coding:utf-8

"""

Number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""

'''
Clue:
The number on the up right conner is n^2 (n=1,3,5....)
'''

def answer():
	m=1
	for i in xrange(3,1003,2):
		m+=sum([i**2-(i-1)*j for j in xrange(4)])
	print m

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 669171001
# run time= 0.00102686882019