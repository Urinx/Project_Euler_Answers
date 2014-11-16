#!/usr/bin/env python
#coding:utf-8

"""
Counting block combinations II

NOTE: This is a more difficult version of Problem 114.
A row measuring n units in length has red blocks with a minimum length of m units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.
Let the fill-count function, F(m, n), represent the number of ways that a row can be filled.
For example, F(3, 29) = 673135 and F(3, 30) = 1089155.
That is, for m = 3, it can be seen that n = 30 is the smallest value for which the fill-count function first exceeds one million.
In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and F(10, 57) = 1148904, so n = 57 is the least value for which the fill-count function first exceeds one million.
For m = 50, find the least value of n for which the fill-count function first exceeds one million.

"""
def F(m,n):
	ways = [1] * (n+1)

	for j in range(m, n+1):
	    ways[j] = ways[j - 1] + 1
	    for k in range(m, j):
	        ways[j] += ways[j - k - 1]

	return ways[n]

def answer():
	m,n=50,100
	MAX=1000000
	while F(m,n)<=MAX:
		n+=1
	print n

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 168
# run time= 0.0728759765625