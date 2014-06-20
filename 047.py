#!/usr/bin/env python
#coding:utf-8

"""

Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

"""
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

def prime_factor_numbers(num):
    n=0
    for p in primes:
        if p>num/2: break
        if num%p==0: n+=1
    return n

def anwser():
    i=210
    a=[]
    while 1:
        if prime_factor_numbers(i)==4:
            if len(a)==3:
                print a[0]
                break
            else: a.append(i)
        else: a=[]
        i+=1

import time
tStart=time.time()
primes=[]
for p in gen_primes():
    if p>10000: break
    primes.append(p)
anwser()
print 'run time=',time.time()-tStart
# 134043
# run time= 23.6665558815