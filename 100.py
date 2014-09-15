#!/usr/bin/env python
#coding:utf-8

"""
Arranged probability

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

"""

'''
X0=1
Y0=1
Xn+1=3Xn+2Yn-2
Yn+1=4Xn+3Yn-3
'''

def answer():
	b=1
	n=1
	while 1:
		if n>1e12: break
		b,n=3*b+2*n-2,4*b+3*n-3
	print b

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 756872327473
# run time= 9.20295715332e-05