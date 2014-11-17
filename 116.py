#!/usr/bin/env python
#coding:utf-8

"""
Red, green or blue tiles

A row of five black square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).
If red tiles are chosen there are exactly seven ways this can be done.
If green tiles are chosen there are three ways.
And if blue tiles are chosen there are two ways.
Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the black tiles in a row measuring five units in length.
How many different ways can the black tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?
NOTE: This is related to Problem 117.

"""
def F(m,n):
	ways = [1] * (n+1)

	for j in range(m, n+1):
	    ways[j] = ways[j - 1] + 1
	    for k in range(m, j):
	        ways[j] += ways[j - k - 1]

	return ways[n]

def answer():
	total=0
	for i in xrange(3,50):
		total+=F(i,50)
	print total

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 17420911235
# run time= 0.00830507278442