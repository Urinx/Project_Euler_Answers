#!/usr/bin/env python
#coding:utf-8

"""

Quadratic primes

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

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

def is_prime(num):
	if num<=0: return False
	for i in p:
		if num%i==0: return False
		if i>num/2+1: break
	return True

def euler_formula(a,b,n):
	return n**2+a*n+b

def anwser():
	m=0
	for a in xrange(-999,1000):
		for b in xrange(1,1000):
			n=0
			while is_prime(euler_formula(a,b,n)):
				n+=1
			if n>=m:
				m=n
				c=[a,b]
	print m,c,c[0]*c[1]

import time
tStart=time.time()

p=[]
for i in gen_primes():
	if i>1000: break
	p.append(i)

anwser()

print 'run time=',time.time()-tStart
# -59231
# run time= 5.44322800636