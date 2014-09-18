#!/usr/bin/env python
#coding:utf-8

"""
Triangle containment

Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.
Consider the following two triangles:
A(-340,495), B(-153,-910), C(835,-947)
X(-175,41), Y(-421,-714), Z(574,-645)
It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.
NOTE: The first two examples in the file represent the triangles in the example given above.

"""

def CrossProduct(A,B):
	return A[0]*B[1]-A[1]*B[0]

def answer():
	with open('p102_triangles.txt','r') as f:
		total=0
		for line in f.readlines():
			dot=[int(n) for n in line.replace('\n','').split(',')]
			OA=dot[:2]
			OB=dot[2:4]
			OC=dot[4:]
			a=CrossProduct(OA,OB)
			b=CrossProduct(OB,OC)
			c=CrossProduct(OC,OA)
			if (a>0 and b>0 and c>0) or (a<0 and b<0 and c<0):
				total+=1
		print total

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 228
# run time= 0.0154139995575