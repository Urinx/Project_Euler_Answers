#!/usr/bin/env python
#coding:utf-8

"""

1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

"""

def Fibonacci():
	a=[1,1]
	while True:
		a.append(sum(a))
		yield a.pop(0)

def answer():
	a=0
	for i in Fibonacci():
		a+=1
		if len(str(i))>=1000:
			print a
			break

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 4782
# run time= 0.0710821151733