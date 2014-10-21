#!/usr/bin/env python
#coding:utf-8

"""
Primes with runs

Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and so on. But there are nine 4-digit primes containing three ones:
1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111
We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime where d is the repeated digit, N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes.
So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.
In the same way we obtain the following results for 4-digit primes.
Digit, d	M(4, d)	N(4, d)	S(4, d)
0	2	13	67061
1	3	9	22275
2	3	1	2221
3	3	12	46214
4	3	2	8888
5	3	1	5557
6	3	1	6661
7	3	9	57863
8	3	1	8887
9	3	7	48073
For d = 0 to 9, the sum of all S(4, d) is 273700.
Find the sum of all S(10, d).

"""
import math
import itertools

def is_prime(num):
	if num==2: return True
	if num%2==0 or num<=0: return False
	for i in xrange(3,int(math.sqrt(num))+1,2):
		if num%i==0: return False
	return True

def templet(n):
	temp=[]
	k=10-n
	for i in itertools.combinations(range(10),k):
		t=['#']*10
		for j in range(k):
			t[i[j]]='{'+str(j)+'}'
		temp.append(''.join(t))
	return temp

def pformat(t,i,j,k):
	if i==0 and t[0]=='#': return -1
	t=t.replace('#',str(i))
	for p in range(k):
		t=t.replace('{'+str(p)+'}',str(j[p]))
	if t[0]=='0': return -1
	return int(t)

def answer():
	result=0
	a=range(10)
	c=[]
	for n in range(9,0,-1):
		a=list(set(a)-set(c))
		if not a: break
		temp=templet(n)
		k=10-n
		c=[]

		for i in a:
			b=range(10)
			b.remove(i)
			for j in itertools.product(b,repeat=k):
				for t in temp:
					num=pformat(t,i,j,k)
					if is_prime(num):
						result+=num
						if i not in c: c.append(i)

	print result

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 612407567715
# run time= 0.44299197197