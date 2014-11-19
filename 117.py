#!/usr/bin/env python
#coding:utf-8

"""
Red, green, and blue tiles

Using a combination of black square tiles and oblong tiles chosen from: red tiles measuring two units, green tiles measuring three units, and blue tiles measuring four units, it is possible to tile a row measuring five units in length in exactly fifteen different ways.
How many ways can a row measuring fifty units in length be tiled?
NOTE: This is related to Problem 116.

"""
def answer():
	ways, n = [1, 2, 4, 8], 50
	while len(ways) < n:
		ways+=[sum(ways[-4:])]
	print ways[-1]

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 100808458960497
# run time= 0.000127077102661