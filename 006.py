#!/usr/bin/env python
#coding:utf-8

'''

Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is 
3025 − 385 = 2640.
Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.

'''

def anwser():
	print (101*50)**2-sum(map(lambda x:x**2,xrange(0,101)))

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
#25164150