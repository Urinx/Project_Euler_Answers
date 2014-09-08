#!/usr/bin/env python
#coding:utf-8

"""
Arithmetic expressions

By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.
For example,
8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)
Note that concatenations of the digits, like 12 + 34, are not allowed.
Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.
Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.

"""
import itertools

def answer():
	param=[
	['#1','#2','#3','#4'],
	['(#1','#2)','#3','#4'],
	['#1','(#2','#3)','#4'],
	['#1','#2','(#3','#4)'],
	['(#1','#2','#3)','#4'],
	['#1','(#2','#3','#4)'],
	['(#1','#2)','(#3','#4)'],
	['((#1','#2)','#3)','#4'],
	['(#1','(#2','#3))','#4'],
	['#1','((#2','#3)','#4)'],
	['#1','(#2','(#3','#4))'],
	]
	operations=['*','+','/','-']
	f=[]
	for i in itertools.product(operations,repeat=3):
		f.extend([j[0]+i[0]+j[1]+i[1]+j[2]+i[2]+j[3] for j in param])

	result={}
	for i in itertools.combinations([str(t)+'.' for t in range(10)],4):
		tmp=[]
		for a,b,c,d in itertools.permutations(i,4):
			for j in f:
				ev=j.replace('#1',a).replace('#2',b).replace('#3',c).replace('#4',d)
				try:
					r=eval(ev)
					if r>0 and r.is_integer():
						tmp+=[int(r)]
				except Exception, e:
					pass
		result[i]=sorted(list(set(tmp)))

	m=[0,1]
	for i,r in result.items():
		for j,k in enumerate(r):
			if j!=k-1:
				n=k
				break
		if n>m[1]:
			m=[i,n]
	print ''.join(m[0])

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 1258
# run time= 60.0827469826