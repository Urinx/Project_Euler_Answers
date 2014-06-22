#!/usr/bin/env python
#coding:utf-8

"""

Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?

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

primes=[]
for p in gen_primes():
	if p>1000: break
	primes.append(p)

def is_prime(num):
    for p in primes:
        if p>math.sqrt(num): break
        if num%p==0: return False
    return True

def is_arithmetic_sequence(arr):
	if len(set(map(lambda x,y:x-y,arr[1:],arr[:-1])))==1: return True
	return False

def anwser():
	for i in xrange(1001,3338):
		if is_prime(i) and is_prime(i+3330) and is_prime(i+6660) and set(str(i))==set(str(i+3330))==set(str(i+6660)):
			print i,i+3330,i+6660

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 1487 4817 8147
# 2969 6299 9629
# run time= 0.00776100158691