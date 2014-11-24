#!/usr/bin/env python
#coding:utf-8

"""
Disc game prize fund

A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.
The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.
If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.
Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.

"""
from math import factorial

def answer():
	n = 15
	r = (n-1) // 2
	p = [1] + [0]*r
	for k in range(n+1):
	    for i in range(r, 0, -1):
	        p[i] += k * p[i-1]
	print factorial(n+1) / sum(p)

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 2269
# run time= 0.000174045562744