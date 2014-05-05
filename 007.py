#!/usr/bin/env python
#coding:utf-8

'''

10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, 
and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

'''

def primes_until_n(n):
    prime=[2]
    m=3
    while len(prime)<n:
        i=0
        while prime[i]**2<=m:
            if m%prime[i]==0:
                m+=2
                i=1
            else:i+=1
        prime.append(m)
        m+=2
    return prime

def anwser():
	primes=primes_until_n(10001)
	print primes

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
#104743