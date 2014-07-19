#!/usr/bin/env python
#coding:utf-8

"""
Digit factorial chains

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145
Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872
It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)
Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

"""
from math import factorial as f

def foo(num):
	a=[num]
	while 1:
		tmp=sum([f(int(i)) for i in list(str(a[-1]))])
		if tmp in a: break
		a.append(tmp)
	return len(a)

b={}
def foo2(num):
	a=[num]
	while 1:
		if a[-1] in b: tmp=b[a[-1]]
		else:
			tmp=sum([f(int(i)) for i in list(str(a[-1]))])
			b[a[-1]]=tmp
		if tmp in a: break
		a.append(tmp)
	return len(a)

def answer():
    m=0
    for i in xrange(1000000):
        if foo2(i)==60: m+=1
    print m

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 402
# foo:  run time= 136.037657976
# foo2: run time= 25.4294519424