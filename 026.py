#!/usr/bin/env python
#coding:utf-8

"""

Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""

def foo(m,n):
	while m%n!=0:
		if m/n==0:
			yield (0,m)
			m*=10
		else:
			yield (m/n,m%n)
			m=m%n*10
	yield (m/n,0)

def bar(m,n):
	a=[]
	for i in foo(m,n):
		if i in a: return len(a)-a.index(i)
		a.append(i)

def answer():
    m=d=0
    for n in xrange(2,1000):
    	t=bar(1,n)
    	if t>m:m,d=t,n
    print d

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 983
# run time= 0.610565900803