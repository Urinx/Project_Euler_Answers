#!/usr/bin/env python
#coding:utf-8

"""

Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
	d2d3d4=406 is divisible by 2
	d3d4d5=063 is divisible by 3
	d4d5d6=635 is divisible by 5
	d5d6d7=357 is divisible by 7
	d6d7d8=572 is divisible by 11
	d7d8d9=728 is divisible by 13
	d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

"""
p=[2,3,5,7,11,13,17]

def made_by_nums(d):
	if len(d)==1: return [d[0]]
	a=[]
	for i in xrange(len(d)-1,-1,-1):
		t=d[:]
		t.pop(i)
		for j in made_by_nums(t):
			a.append(d[i]+j)
	return a

def with_this_property(s):
	for i in xrange(1,8):
		if int(s[i:i+3])%p[i-1]!=0: return False
	return True

def anwser():
	m=0
	a=made_by_nums([str(i) for i in range(10)])
	while a[-1][0]=='0':
		a.pop()
	for n in a:
		if with_this_property(n): m+=int(n)
	print m

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 16695334890
# run time= 18.5190529823