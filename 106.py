#!/usr/bin/env python
#coding:utf-8

"""
Special subset sums: meta-testing

Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:
S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
For this problem we shall assume that a given set contains n strictly increasing elements and it already satisfies the second rule.
Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4, only 1 of these pairs need to be tested for equality (first rule). Similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.
For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?
NOTE: This problem is related to Problem 103 and Problem 105.

"""
def fact(n):
    "factorial"
    return reduce(lambda x, y: x * y, range(1, n + 1))

def nCr(n, r):
    "n choose r"
    if n == r:
        return 1
    else:
        return fact(n) / (fact(r) * fact(n - r))

def x_with_x(n, x):
    "number of *disjoint* x-subset pairs one can form with an array of length n"
    if n - x >= x:
        return (nCr(n, x) * nCr(n - x, x)) / 2
    else:
        return 0

catalans = {2:2, 3:5, 4:14, 5:42, 6:132}

def dominated(n, x):
    "number of 'strictly dominated' x_with_x guys -- these need not be checked"
    return nCr(n, 2 * x) * catalans[x]

def need_to_check(n):
    "number of disjoint subset pairs we need to check for array length n"
    tot = 0
    for x in range(2, n // 2 + 1):
        tot += x_with_x(n, x) - dominated(n, x)
    return tot

def answer():
	print need_to_check(12)

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 21384
# run time= 0.000514984130859