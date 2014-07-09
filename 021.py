#!/usr/bin/env python
#coding:utf-8

"""

Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers 
less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an 
amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 
20, 22, 44, 55 and 110; therefore d(220) = 284. The proper 
divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""
def divisors_sum(num):
	divisors=[1]
	for i in xrange(2,num/2+1):
		if num%i==0:
			divisors.append(i)
	return sum(divisors)

def answer():
    amicable_num=[]
    for i in xrange(4,10000):
    	m=divisors_sum(i)
    	if i in amicable_num:
    		continue
    	elif i==divisors_sum(m) and i!=m:
    		amicable_num.append(i)
    		amicable_num.append(m)
    		print i,m
    print 'Sum=',sum(amicable_num)

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 48942
# run time= 3.24885010719