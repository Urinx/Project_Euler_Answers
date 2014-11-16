#!/usr/bin/env python
#coding:utf-8

"""
Counting block combinations I

A row measuring seven units in length has red blocks with a minimum length of three units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square. There are exactly seventeen ways of doing this.
How many ways can a row measuring fifty units in length be filled?
NOTE: Although the example above does not lend itself to the possibility, in general it is permitted to mix block sizes. For example, on a row measuring eight units in length you could use red (3), black (1), and red (4).

"""
def answer():
	m, n = 3, 50
	ways = [1] * (n+1)

	for j in range(m, n+1):
	    ways[j] = ways[j - 1] + 1
	    for k in range(m, j):
	        ways[j] += ways[j - k - 1]

	print "Minimum block size =", m, "units"
	print "A space", n, "units long can be filled", ways[n], "ways"

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 16475640049
# run time= 0.000578880310059