#!/usr/bin/env python
#coding:utf-8

"""

Coin sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

"""

def anwser():
	s=7
	for a in xrange(0,2):
		for b in xrange(0,4):
			for c in xrange(0,10):
				for d in xrange(0,20):
					for e in xrange(0,40):
						for f in xrange(0,100):
							m=100*a+50*b+20*c+10*d+5*e+2*f
							if m<=200: s+=1
	print s

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 73682
# run time= 1.96884202957