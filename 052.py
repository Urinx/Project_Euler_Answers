#!/usr/bin/env python
#coding:utf-8

"""

Permuted multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""

def answer():
    i=10000
    while 1:
        x=int('1'+str(i))
        if set(str(x))==set(str(2*x))==set(str(3*x))==set(str(4*x))==set(str(5*x))==set(str(6*x)):
            print x
            break
        i+=1

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 142857
# run time= 0.132374048233