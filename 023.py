#!/usr/bin/env python
#coding:utf-8

"""

Non-abundant sums

A perfect number is a number for which the sum of its proper divisors 
is exactly equal to the number. For example, the sum of the proper 
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 
is a perfect number.

A number n is called deficient if the sum of its proper divisors is 
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the 
smallest number that can be written as the sum of two abundant numbers 
is 24. By mathematical analysis, it can be shown that all integers 
greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed 
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written 
as the sum of two abundant numbers.

"""

def divisors_sum(num):
	d=[1]
	for i in xrange(2,num/2+1):
		if num%i==0:
			d.append(i)
	return sum(d)

def is_perfect_number(num):
	if num==divisors_sum(num):
		return True
	return False

def is_abundant_number(num):
	if num<divisors_sum(num):
		return True
	return False

def abundant_numbers(limit):
	abd_num=[12]
	for i in xrange(13,limit+1):
		if is_abundant_number(i):
			abd_num.append(i)
	return abd_num

def answer():
	two_abd=range(24)
	abd=abundant_numbers(28123/2)
	for i in xrange(25,28124):
		for j in abd:
			if j>=i:
				break
			if not is_abundant_number(i-j):
				two_abd.append(i)
				break
	print sum(two_abd)

def PE023(limit=28123):
	somDiv=[1]*(limit+1)
	for i in range(2,int(limit**.5)+1):
		somDiv[i*i]+=i
		for k in range(i+1,limit//i+1):
			somDiv[k*i]+=k+i
	abondant,res=set(),0
	ajout=abondant.add
	for n in range(1,limit+1):
		if somDiv[n]>n: ajout(n)
		if not any((n-a in abondant) for a in abondant): res+=n
	return res

import time
tStart=time.time()
#answer()
print PE023()
print 'run time=',time.time()-tStart
# 4179871
# run time= 0.652102947235