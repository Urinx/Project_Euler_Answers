#!/usr/bin/env python
#coding:utf-8

"""

Longest Collatz sequence

The following iterative sequence is defined for the set of
positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the
following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing
at 1) contains 10 terms. Although it has not been proved yet
(Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

"""

def collatz(num):
	if num not in c:
		if num%2==0:
			l=1+collatz(num/2)
		else:
			l=1+collatz(3*num+1)
		c[num]=l
	return c[num]

c={1:1,2:2,3:8,4:3,5:6}

def answer():
	m,n=0,0
	for i in xrange(6,1000001):
		l=collatz(i)
		if l>m:
			m,n=l,i
	print n

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 837799
# run time= 1.95199012756