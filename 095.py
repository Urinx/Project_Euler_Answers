#!/usr/bin/env python
#coding:utf-8

"""
Amicable chains

The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.
Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.
Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)
Since this chain returns to its starting point, it is called an amicable chain.
Find the smallest member of the longest amicable chain with no element exceeding one million.

"""
def answer():
	limit=1000000
	divisors_sum={1:[1]}
	for i in xrange(2,limit+1): divisors_sum[i]=[]
	for i in xrange(1,limit/2+1):
		a=2*i
		while a<=limit:
			divisors_sum[a].append(i)
			a+=i
	for i in xrange(1,limit+1):
		s=sum(divisors_sum[i])
		if s>=limit: del(divisors_sum[i])
		else: divisors_sum[i]=s

	flag=1
	while flag:
		flag=0
		for i,j in divisors_sum.items():
			if j not in divisors_sum or i==j:
				del(divisors_sum[i])
				flag=1

	chain={}
	for i,j in divisors_sum.items():
		tmp=[i]
		t=j
		while t not in tmp:
			tmp+=[t]
			t=divisors_sum[t]
		if len(tmp[tmp.index(t):])>1:
			chain[tuple(tmp)]=len(tmp[tmp.index(t):])

	m=[0,0]
	for i,j in chain.items():
		if j>m[1]:
			m=[min(i),j]
	print m[0]

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 14316
# run time= 12.3490931988