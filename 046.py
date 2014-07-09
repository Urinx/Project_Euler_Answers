#!/usr/bin/env python
#coding:utf-8

"""

Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

"""
import math,itertools

def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q        
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def answer():
	primes=[]
	b=[2*i*i for i in xrange(1,100)]
	for p in gen_primes():
		if p>10000: break
		primes.append(p)

	for o in xrange(17,10000):
		o=2*o+1
		s=1
		if o not in primes:
			for p in primes:
				if p>=o: break
				if o-p in b:
					s=0
					break
			if s:
				print o
				return

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 5777
# run time= 0.27857208252