#!/usr/bin/env python
#coding:utf-8

"""
Bouncy numbers

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
Find the least number for which the proportion of bouncy numbers is exactly 99%.

"""
def isIncNum(n):
	d=[int(i) for i in list(str(n))]
	return all(map(lambda x,y:x<=y,d[:-1],d[1:]))

def isDecNum(n):
	d=[int(i) for i in list(str(n))]
	return all(map(lambda x,y:x>=y,d[:-1],d[1:]))

def isBouncyNum(n):
	if isIncNum(n) or isDecNum(n): return False
	return True

def answer():
	bouncy=525
	n=1000

	while 1:
		if isBouncyNum(n): bouncy+=1
		if n%100==0 and n/100*99==bouncy: break
		n+=1
	print n

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 1587000
# run time= 21.3708519936