#!/usr/bin/env python
#coding:utf-8

"""
Square digit chains

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
For example,
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?

"""
def next(n):
	return sum(int(i)**2 for i in str(n))

def answer():
	tmp={1:0,89:1}
	for i in xrange(2,10000000):
		n,t=i,[]
		while 1:
			t+=[n]
			if n in tmp: break
			n=next(n)
		for j in t[:-1]:
			tmp[j]=tmp[n]
	print sum(tmp.values())

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 8581146
# run time= 68.4451868534