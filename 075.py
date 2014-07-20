#!/usr/bin/env python
#coding:utf-8

"""
Singular integer right triangles

It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.
12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)
In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
120 cm: (30,40,50), (20,48,52), (24,45,51)
Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

"""
import math

def hcf(a,b):
    if b==0: return a
    return hcf(b,a%b)

def answer():
    t,result={},0
    limit=int(math.sqrt(1500000/2))
    for m in xrange(2,limit):
        for n in xrange(1,m):
            if (m+n)%2==1 and hcf(n,m)==1:
                l=2*m*(m+n)
                while l<1500000:
                    if not t.has_key(l): t[l]=0
                    t[l]+=1
                    if t[l]==1: result+=1
                    if t[l]==2: result-=1
                    l+=2*m*(m+n)
    print result

def answer_slow():
    m=0
    for l in xrange(12,1500001,2):
    	t=0
    	for c in xrange(l/3,l/2):
    		delta=c**2+2*l*c-l**2
    		if delta<0: continue
    		tmp=int(delta**0.5)
    		if tmp**2==delta and (l-c-tmp)%2==0: t+=1
    		if t>1: break
    	if t==1: m+=1
    print m

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 161667
# run time= 1.49876499176