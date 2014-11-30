#!/usr/bin/env python
#coding:utf-8

"""
Palindromic sums

The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.
There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with the squares of positive integers.
Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares.

"""

from projecteuler import is_palindromic

L = 10**8
sqrt_limit = int(L ** 0.5)    
pal = set()

for i in range(1, sqrt_limit-1):
    sos = i*i
    for j in xrange(i+1, sqrt_limit):
        sos += j*j
        if sos >= L: break
        if is_palindromic(sos): pal.add(sos)

print "Answer to PE125 =", sum(pal), len(pal)
# 2906969179