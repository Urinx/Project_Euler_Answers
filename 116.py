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
	ways = [1] * m + [0] * (n-m+1)
	for j in range(m, n+1):
	    ways[j] += ways[j-1] + ways[j - m]
	return ways[n]-1

def answer():
	print F(2,50)+F(3,50)+F(4,50)

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 20492570929
# run time= 0.000205993652344