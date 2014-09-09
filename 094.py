#!/usr/bin/env python
#coding:utf-8

"""
Almost equilateral triangles

It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.
We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.
Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

"""
import math

def answer_slow():
	m=0
	for i in xrange(2,333333333):
		for j in (i-1,i+1):
			s=math.sqrt(4*i*i-j*j)/2
			if s.is_integer():
				m+=2*i+j
	print m

def answer():
	x,y=2,1
	limit=1000000000
	result=0

	while 1:
		for i in (1,-1):
			aTimes3=2*x-i
			areaTimes3=y*(x-2*i)
			if aTimes3>limit:
				print result
				return
			if aTimes3>0 and areaTimes3>0 and aTimes3%3==0 and areaTimes3%3==0:
				a=aTimes3/3
				result+=3*a+i
		x,y=2*x+3*y,2*y+x

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 518408346
# run time= 0.00012993812561