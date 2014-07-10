#!/usr/bin/env python
#coding:utf-8

"""
Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

"""
import math,itertools

def is_prime(num):
    if num<=0: return False
    if num in primes: return True
    for p in primes:
        if p>math.sqrt(num): break
        if num%p==0: return False
    return True

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

def foo(m,n):
    if is_prime(int(str(m)+str(n))) and is_prime(int(str(n)+str(m))): return True
    return False

def bar(m,n,l):
    if foo(m,n) and foo(m,l) and foo(n,l): return True
    return False

primes=[]
for p in gen_primes():
    if p>8400: break
    primes.append(p)

def answer():
    s={}
    for i in itertools.combinations(primes[1:],2):
        if i[0]>5500: break
        if foo(*i):
            if s.has_key(i[0]): s[i[0]].append(i[1])
            else: s[i[0]]=[i[1]]
    for i in itertools.combinations(sorted(s.keys()),2):
        if i[1] in s[i[0]]:
            u=sorted(set(s[i[0]]) & set(s[i[1]]))
            if u and len(u)>=3:
                for j in itertools.combinations(u,3):
                    if bar(*j):
                        print sum(i+j)
                        break

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 26033
# run time= 23.2336580753