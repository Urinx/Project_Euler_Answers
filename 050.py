#!/usr/bin/env python
#coding:utf-8

"""

Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""
import math

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
    if p>10000: break
    primes.append(p)

def is_prime(num):
    for p in primes:
        if p>math.sqrt(num): break
        if num%p==0: return False
    return True

def anwser():
    m=[0,0]
    for i in xrange(0,29):
        for j in xrange(len(primes)-680,i,-1):
            s=sum(primes[i:j])
            if s<1000000 and is_prime(s) and j-i>m[1]:
                m=[s,j-i]
                break
    print m,len(primes)

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# [997651, 543]
# run time= 0.111933946609