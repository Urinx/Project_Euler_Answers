#!/usr/bin/env python
#coding:utf-8

"""
Coin partitions

Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.
    OOOOO
   OOOO   O
   OOO   OO
  OOO   O   O
  OO   OO   O
 OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.

"""

'''
http://zh.wikipedia.org/wiki/%E4%BA%94%E9%82%8A%E5%BD%A2%E6%95%B8%E5%AE%9A%E7%90%86
'''

def p(n):
    return n*(3*n-1)/2

def answer():
    n=101
    P=n*[0]
    P[0]=1
    T=[p(j) for i in xrange(1,700) for j in [i,-i]]

    for i in xrange(1,n):
        for j in xrange(i,n):
            P[j]+=P[j-i]

    while 1:
        P+=[0]
        for m in xrange(0,len(T)):
            if n-T[m]<0: break
            if m%4>1: a=-1
            else: a=1
            P[n]+=a*P[n-T[m]]
        if P[n]%1000000==0: break
        n+=1

    print 'n:',len(P)-1
    print 'P(n):',P[-1]

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 55374
# run time= 8.69310092926
