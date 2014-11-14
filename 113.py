#!/usr/bin/env python
#coding:utf-8

"""
Non-bouncy numbers

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 10^10.
How many numbers below a googol (10^100) are not bouncy?

"""
def numOfIncreasing(n):
	return C(n+9,n)-1

def numOfDecreasing(n):
	return C(n+10,n)-1

def numOfDuplicates(n):
	return 10*n

def C(m,n):
	return reduce(lambda x,y:x*y,xrange(m-n+1,m+1))/reduce(lambda x,y:x*y,xrange(1,n+1))

def answer():
	n=100
	print numOfIncreasing(n)+numOfDecreasing(n)-numOfDuplicates(n)

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 51161058134250
# run time= 0.000545024871826