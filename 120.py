#!/usr/bin/env python
#coding:utf-8

"""
Square remainders

Let r be the remainder when (a−1)n + (a+1)n is divided by a2.
For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.
For 3 ≤ a ≤ 1000, find ∑r(max).

"""
def answer():
	L = 1000
	print "Sum of R(max) for 3 <= a <=", L, "=", L**3 // 3 - L**2 // 4 - L*5 // 6

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 333082500
# run time= 9.01222229004e-05