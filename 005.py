#!/usr/bin/env python
#coding:utf-8

'''

Smallest multiple

2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?

'''

def primes_lessthan_max(max):
    prime=[2]
    m=3
    while prime[-1]<max:
        i=0
        while prime[i]**2<=m:
            if m%prime[i]==0:
                m+=2
                i=1
            else:i+=1
        prime.append(m)
        m+=2
    prime.pop()
    return prime

def anwser():
	primes=primes_lessthan_max(20)
	n=[]
	for p in primes:
		m=0
		for i in xrange(p,21):
			a=0
			while i%p==0:
				i=i/p
				a+=1
			if a>m:
				m=a
		n.append(m)
	print primes
	print n
	print reduce(lambda x,y:x*y,map(lambda x,y:x**y,primes,n))

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
#232792560