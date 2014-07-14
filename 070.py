#!/usr/bin/env python
#coding:utf-8

"""
Totient permutation

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

"""
import math,itertools

def gen_primes():
    D={}
    q=2
    while True:
        if q not in D:
            yield q        
            D[q*q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p+q,[]).append(p)
            del D[q]
        q+=1

def answer():
    ps=[]
    for p in gen_primes():
        if p>4000: break
        ps.append(p)
    m=[0,10]
    for i in itertools.combinations(ps,2):
        n=i[0]*i[1]
        t=(i[0]-1)*(i[1]-1)
        ratio=float(n)/t
        if n<1e7 and ratio<m[1] and sorted(str(n))==sorted(str(t)):
            m=[n,ratio]
    print m[0]

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 8319823
# run time= 0.336660146713