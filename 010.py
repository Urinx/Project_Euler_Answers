#!/usr/bin/env python
#coding:utf-8

'''

Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

'''

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
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

def anwser1():
    result=0
    primes=gen_primes()
    for p in primes:
        if p>=2000000:
            print result
            break
        else:
            result+=p

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

def anwser2():
    primes=primes_lessthan_max(2000000)
    print sum(primes)

import time
tStart=time.time()
anwser1()
print 'run time=',time.time()-tStart
# Answer 1
# 142913828922
# run time= 2.66002297401

# Answer 2
# run time= 7.71048307419