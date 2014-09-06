#!/usr/bin/env python
#coding:utf-8

"""
Right triangles with integer coordinates

The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.
There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.
Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?

"""
import itertools

def is_right_angle(i,j):
	a=i[0]**2+i[1]**2
	b=j[0]**2+j[1]**2
	c=(i[0]-j[0])**2+(i[1]-j[1])**2
	return a+b==c or a+c==b or b+c==a

def answer():
	limit=50
	points=[(i,j) for i in xrange(limit+1) for j in xrange(limit+1)][1:]
	print sum([1 for i,j in itertools.combinations(points,2) if is_right_angle(i,j)])

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 14234
# run time= 3.55255103111