#!/usr/bin/env python
#coding:utf-8

"""
abc-hits

The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.
We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:
GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c
For example, (5, 27, 32) is an abc-hit, because:
GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32
It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.
Find ∑c for c < 120000.

"""

from mathplus import timer, gcd, sqrt, isqrt

M = 120000

@timer
def pe(M):
    rad = [0] * M
    rad[1] = 1
    for p in range(2, M):
        if rad[p] > 0: continue
        isqrtp = isqrt(p)
        flag = True
        for q in range(2, isqrtp + 1):
            if p % q != 0: continue
            pp = p
            while pp % q == 0:
                pp //= q
            qq = q * rad[pp]
            pp = p
            while pp < M:
                rad[pp] = qq
                pp *= q
            flag = (q > isqrtp)
            break
        if flag:
            pp = p
            while pp < M:
                rad[pp] = p
                pp *= p

    s = 0
    for c in range(3, M):
        cc = (c-1)//rad[c]
        if rad[c-1] <= cc:
            s += c
        if cc < 6: continue
        if c % 2 == 0 and cc < 15: continue
        if c % 3 == 0 and cc < 10: continue
        for a in range(2, c//2):
            b = c - a
            if rad[a] > cc or rad[b] > cc: continue
            if rad[a] * rad[b] <= cc and gcd(a, b) == 1:
                s += c
    return s

print(pe(M))
# 21417
# run time= 0.381587982178