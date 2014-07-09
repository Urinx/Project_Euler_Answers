#!/usr/bin/env python
#coding:utf-8

"""

Circular primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?

"""
def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q        
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def c_p(ps):
	b=[]
	for p in ps:
		t=s=str(p)
		a=1
		if s in b: break
		while 1:
			t=t[1:]+t[0]
			if t==s: break
			if int(t) not in ps:
				a=0
				break
			ps.remove(int(t))
		if a: b.append(s)
	return b

def answer():
	primes3=[]
	primes4=[]
	primes5=[]
	primes6=[]
	m=13
	for i in gen_primes():
		if i>=1000000: break
		l=list(str(i))
		if '0' in l or '2' in l or '4' in l or '6' in l or '8' in l: continue
		if i>=100000:
			primes6.append(i)
			continue
		if i>=10000:
			primes5.append(i)
			continue
		if i>=1000:
			primes4.append(i)
			continue
		if i>=100: primes3.append(i)
	for i in xrange(3,7):
		m+=len(c_p(eval('primes'+str(i))))*i
	print m
	

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 55
# run time= 1.498057127