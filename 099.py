#!/usr/bin/env python
#coding:utf-8

"""
Largest exponential

Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.
However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.
Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
NOTE: The first two lines in the file represent the numbers in the example given above.

"""
import math

def answer():
	with open('base_exp.txt','r') as f:
		m,t=[0,0],1
		for n in [i.replace('\r\n','').split(',') for i in f.readlines()]:
			a,b=int(n[0]),int(n[1])
			tmp=b*math.log(a)
			if tmp>m[0]: m=[tmp,t]
			t+=1
	print m[1]

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 709
# run time= 0.00477313995361