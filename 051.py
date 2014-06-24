#!/usr/bin/env python
#coding:utf-8

"""

Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

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

def is_prime(num):
    for p in primes:
        if p>math.sqrt(num): break
        if num%p==0: return False
    return True

def prime_number(i,d):
    a=0
    for j in xrange(10-int(d)):
        t=int(str(i).replace(d,str(j+int(d))))
        if is_prime(t): a+=1
    return a

primes=[]

def anwser():
    for p in gen_primes():
        if p>56003:
            for d in set(['0','1','2']) & set(str(p)):
                if prime_number(p,d)>=8:
                    print p
                    return
        if p<10000: primes.append(p)

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 121313
# run time= 0.790215015411