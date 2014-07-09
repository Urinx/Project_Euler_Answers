#!/usr/bin/env python
#coding:utf-8

"""

Spiral primes

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

"""
import math

def is_prime(num):
	if num%2==0 or num<=0: return False
	for i in xrange(3,int(math.sqrt(num))+1,2):
		if num%i==0: return False
	return True

def answer():
	n,p=7,8.
	while 1:
		n+=2
		total=2*n-1
		for j in [n**2-x*(n-1) for x in range(4)]:
			if is_prime(j): p+=1
		if p/total<0.1: break
	print n

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 26241
# run time= 3.47689294815