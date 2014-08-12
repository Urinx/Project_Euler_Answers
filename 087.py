#!/usr/bin/env python
#coding:utf-8

"""
Prime power triples

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:
28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24
How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

"""
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

def answer():
    MAX=50000000
    p1_max=int(MAX**0.5)+1
    P=primes_lessthan_max(p1_max)
    nums=set()
    for p3 in P:
        for p2 in P:
            s1=p3**4+p2**3
            if s1>MAX: break
            for p1 in P:
                s2=s1+p1**2
                if s2>MAX: break
                nums.add(s2)
    print len(nums)

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 1097343
# run time= 0.610454082489
