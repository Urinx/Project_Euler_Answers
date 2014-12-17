#!/usr/bin/env python
#coding:utf-8

"""
Repunit divisibility

A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.
Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.
The least value of n for which A(n) first exceeds ten is 17.
Find the least value of n for which A(n) first exceeds one-million.

"""

def gcd(a,b):
    if b > a:
        t = a
        a = b
        b = t
    while (a != b) & (b != 0):
        t = b
        b = a % b
        a = t
    return a


def a(n):
    #print "a({0}) =".format(n),
    ans = 2
    num = 11
    while num != 0:
        if num < n:
            num = num*10 + 1
            ans += 1
        elif num >= n:
            num = (num % n)
    #print ans
    return ans

best = 0
for n in range(1000000,2000000):
    if (n % 1000) == 0:
        print "Trying n = {0}".format(n)

    if gcd(n,10) != 1:
        continue

    an = a(n)

    if an > best:
        best = an
        print "    n = {0}, a({0}) = {1}".format(n, an)

    if an >= 1000000:
        print "Answer found with n = {0}, a({0}) = {1}".format(n, an)
        break

# 1000023