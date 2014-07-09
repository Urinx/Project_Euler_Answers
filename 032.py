#!/usr/bin/env python
#coding:utf-8

"""

Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

"""

'''
9 digits:
[2-8]x@@@@=@@@@
@@x@@@=@@@@

'''

def gen_d(dm):
	dn=[]
	for i in dm:
		a=[str(j) for j in range(1,10)]
		[a.remove(j) for j in list(str(i))]
		for j in a:
			dn.append(int(str(i)+j))
	return dn

def answer():
	d2=gen_d(range(1,10))
	d3=gen_d(d2)
	d4=gen_d(d3)
	r=[]

	for i in xrange(2,9):
		for j in d4:
			if str(i) in list(str(j)): break
			m=i*j
			if m in d4:
				t=1
				for c in list(str(m)):
				 	if c in list(str(i)+str(j)):
				 		t=0
				 		break
				if t and m not in r: r.append(m)

	for i in d2:
		for j in d3:
			if str(i) in list(str(j)): break
			m=i*j
			if m in d4:
				t=1
				for c in list(str(m)):
				 	if c in list(str(i)+str(j)):
				 		t=0
				 		break
				if t and m not in r: r.append(m)
	print sum(r)

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# the correct answer is 45228
# but i dont know where my code is go wrong