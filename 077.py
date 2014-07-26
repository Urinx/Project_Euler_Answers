#!/usr/bin/env python
#coding:utf-8

"""
Prime summations

It is possible to write ten as the sum of primes in exactly five different ways:
7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2
What is the first value which can be written as the sum of primes in over five thousand different ways?

"""
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
    primes=[]
    target=100
    ways=(target+1)*[0]
    ways[0]=1
    for p in gen_primes():
        if p>target: break
        primes.append(p)

    for i in primes:
        for j in xrange(i,target+1):
            ways[j]+=ways[j-i]

    for i in ways:
        if i>=5000:
            print ways.index(i)
            break

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 71
# run time= 0.000764131546021
