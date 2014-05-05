#!/usr/bin/env python

"""

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

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

def primes_until_n(n):
    prime=[2]
    m=3
    while len(prime)<n:
        i=0
        while prime[i]**2<=m:
            if m%prime[i]==0:
                m+=2
                i=1
            else:i+=1
        prime.append(m)
        m+=2
    return prime

def anwser_1():
    a=600851475143
    factor=[]

    def find_factor(n):
        prime=[2]
        m=3
        while n%prime[-1]!=0:
            i=0
            while prime[i]**2<=m:
                if m%prime[i]==0:
                    m+=2
                    i=1
                else:i+=1
            prime.append(m)
            m+=2
        return prime[-1]

    while a!=1:
        f=find_factor(a)
        a=a/f
        factor.append(f)
    print max(factor)

anwser_1()

# Anwser:6857