#!/usr/bin/env python
#coding:utf-8

"""
Prime square remainders

Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn2.
For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.
The least value of n for which the remainder first exceeds 109 is 7037.
Find the least value of n for which the remainder first exceeds 1010.

"""
LIMIT_PRIME = 250000
primes = [0]  # Pad with a dummy item, to make primes[n] return the right thing

def calculate_primes():
    prime_table = [1]*LIMIT_PRIME  # table of largest factor
    i = 2
    while i < (LIMIT_PRIME/2):
        if prime_table[i] == 1:
            primes.append(i)
            j = i*2
            while j < LIMIT_PRIME:
                prime_table[j] = i
                j += i
        i += 1
    while i < LIMIT_PRIME:
        if prime_table[i] == 1:
            primes.append(i)
        i += 1
    del prime_table

def rem_p(n):
    p = primes[n]
    p_sq = p**2
    (pp, pm) = (1,1)
    for i in range(n):
        pp *= (p+1)
        pm *= (p-1)
        pp %= p_sq
        pm %= p_sq
    r = pp + pm
    r = r % p_sq
    return r

def answer():
    calculate_primes()
    print "Found {0} primes".format(len(primes))

    max_res = 0
    for i in range(2,len(primes)):
        res = rem_p(i)
        if res > 10**10:
            print "Answer =", i
            break
    print "Finished without finding result"

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 21035
# run time= 68.5072770119