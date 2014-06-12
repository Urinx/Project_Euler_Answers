#!/usr/bin/env python
#coding:utf-8

"""

Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?

"""

'''
a+b+c=p
a^2+b^2=c^2
	==> a^2+b^2=(a+b-p)^2=(a+b)^2+p^2-2p(a+b)
	==> p^2-2p(a+b)+2ab=0
	==> (p^2/2-pa)/(p-a)=b
'''

def anwser():
	pm=[0,0]
	for p in xrange(12,1000):
		t=0
		for a in xrange(3,p/3):
			m=p**2/2-p*a
			n=p-a
			if m%n==0 and m/n>a:
				t+=1
		if t>pm[0]: pm=[t,p]
	print pm[1]

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 849
# run time= 0.0657351016998