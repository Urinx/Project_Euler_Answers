#!/usr/bin/env python
#coding:utf-8

"""

Powerful digit sum

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

"""
import itertools

def answer():
    m=0
    for i in itertools.permutations(range(1,100),2):
    	t=reduce(lambda x,y:x+int(y),list(str(i[0]**i[1])),0)
    	if t>m: m=t
    print m

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 972
# run time= 0.551580905914