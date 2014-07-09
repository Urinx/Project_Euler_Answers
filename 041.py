#!/usr/bin/env python
#coding:utf-8

"""

Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?

"""
import math

def is_prime(num):
	if num%2==0: return False
	for i in xrange(3,int(math.sqrt(num))+1,2):
		if num%i==0: return False
	return True

def made_by_nums(d):
	if len(d)==1: return [d[0]]
	a=[]
	for i in xrange(len(d)-1,-1,-1):
		t=d[:]
		t.pop(i)
		for j in made_by_nums(t):
			a.append(d[i]+j)
	return a

def answer():
	for n in xrange(10,1,-1):
		for i in made_by_nums([str(i) for i in range(1,n)]):
			if is_prime(int(i)):
				print i
				return

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 7652413
# run time= 1.78753399849