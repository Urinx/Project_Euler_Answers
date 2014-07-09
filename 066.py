#!/usr/bin/env python
#coding:utf-8

"""
Diophantine equation

Consider quadratic Diophantine equations of the form:
x^2 – Dy^2 = 1
For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.
It can be assumed that there are no solutions in positive integers when D is square.
By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1
Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

"""

'''
clue:
http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html
'''
import math

def is_square(num):
    if int(math.sqrt(num))**2==num: return True
    return False

def brute_force():
    x=[3,2,9,5,8]

    for d in xrange(8,1001):
        if is_square(d): continue
        y=1
        while 1:
            m=d*y**2+1
            tmp=int(math.sqrt(m))
            if tmp**2==m:
                x.append(tmp)
                break
            y+=1
    print max(x)

#===========================
def add(i,f):
    return [f[0]+i*f[1],f[1]]

def anti_Continued_Fractions(arr):
    if len(arr)==1: return [arr[0],1]
    return add(arr[0],anti_Continued_Fractions(arr[1:])[::-1])

def sqrt_Continued_Fractions(num):
    a0=int(math.sqrt(num))
    r=[[0,1,a0]]
    while 1:
        p=r[-1][2]*r[-1][1]-r[-1][0]
        q=(num-p**2)/r[-1][1]
        a=(a0+p)/q
        if [p,q,a] in r:
            k=len(r)-r.index([p,q,a])
            break
        r.append([p,q,a])
    return [[i[2] for i in r],k]

def wrong_answer():
    x=[3,2,9,5,8]
    m=[5,9]
    for d in xrange(8,1001):
        if is_square(d): continue
        t=sqrt_Continued_Fractions(d)
        if t[1]%2==0:
            s=anti_Continued_Fractions(t[0][:-1])[0]
        else:
            s=anti_Continued_Fractions(t[0])[0]
        if s>m[1]: m=[d,s]
        x.append(s)
    print m
#===========================
def answer():
    def gao(n):  
        m = int(math.sqrt(n))  
        if m * m == n:  
            return 0 
        ha = 1; ka = 0
        d = m  
        a = n  
        b = -m  
        c = 1
        hb = d; kb = 1
        if hb * hb - n * kb * kb == 1:
            return hb
        while True:  
            nc =  a - b * b  
            nc /= c  
            nd = int((math.sqrt(a) - b) / nc)  
            nb = -b - nd * nc
            c = nc; d = nd; b = nb;
            hc = d * hb + ha
            kc = d * kb + ka
            ha = hb
            ka = kb
            hb = hc
            kb = kc
            if hc * hc - n * kc * kc == 1:
                return hc
        return 0
    ans = 0
    tmp = 0
    for i in range(1, 1001):
        z = gao(i)
        if z > tmp:
            tmp = z
            ans = i
    print ans

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 661
# run time= 0.0125041007996