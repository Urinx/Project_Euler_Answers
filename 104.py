#!/usr/bin/env python
#coding:utf-8

"""
Pandigital Fibonacci ends

The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.
Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

"""

'''
(a+b)≡((a mod c)+(b mod c))(mod c)

O(logN):
	F(2n)=F(n)*(2F(n+1)-F(n))
	F(2n+1)=F(n+1)^2+F(n)^2
'''

def Fibo():
	# Only return the last 9 digits
	a=[1,1]
	while True:
		a.append(sum(a)%1000000000)
		yield a.pop(0)

def F(n):
	if n<=2: return 1
	if n%2==0:
		n/=2
		return F(n)*(2*F(n+1)-F(n))
	else:
		n/=2
		return F(n+1)**2+F(n)**2

def check_last_9_digits(f):
	d=set('123456789')
	s=str(f)
	if len(d-set(s))==0:
		return True
	return False

def check_first_9_digits(n):
	d=set('123456789')
	f=F(n)
	s=str(f)
	if len(d-set(s[:9]))==0:
		return True
	return False

def answer():
	n=1
	for f in Fibo():
		if n>2749:
			if check_last_9_digits(f):
				if check_first_9_digits(n):
					print n
					break
		n+=1

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 329468
# run time= 210.489361048