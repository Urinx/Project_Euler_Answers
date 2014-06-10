#!/usr/bin/env python
#coding:utf-8

"""

Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

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
        q+=1

def anwser():
	p=[]
	m=0
	a=11
	for i in gen_primes():
		if i>1000000: break
		if a==0: break
		s=str(i)
		t=0
		if i>10:
			if s[0] in p and s[-1] in p:
				if i<100: t=1
				if s[1:] in p and s[:-1] in p:
					if i<1000: t=1
					if s[2:] in p and s[:-2] in p:
						if i<10000: t=1
						if s[3:] in p and s[:-3] in p:
							if i<100000: t=1
							if s[4:] in p and s[:-4] in p:
								if i<1000000: t=1
		if t:
			m+=i
			a-=1
		p.append(s)
	print m

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 748317
# run time= 28.1839311123