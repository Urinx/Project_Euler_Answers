#!/usr/bin/env python
#coding:utf-8

'''

Largest palindrome product

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

'''

'''

abccba
9mx
9ny

a=8 or 9
x*y%10=a
(x*y/10+y*m%10+n*x%10)%10=b
...

a=9
[x,y]=[1,9],[3,3],[7,7]

a=8
[x,y]=[1,8],[2,4],[2,9],[3,6],[4,7],[6,8]


'''

def anwser():
	def palindrome_check(p):
		p=str(p)
		if p==p[::-1]:
			return 1
		return 0

	xy=[(1,9),(3,3),(7,7)]
	for i in xy:
		for m in xrange(0,10):
			for n in xrange(0,10):
				n1=int('9'+str(m)+str(i[0]))
				n2=int('9'+str(n)+str(i[1]))
				n3=n1*n2
				if palindrome_check(n3):
					print '{0}={1}*{2}'.format(n3,n1,n2)

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
#906609