#!/usr/bin/env python
#coding:utf-8

"""
Cuboid route

A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.
However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.
By considering all cuboid rooms with integer dimensions, up to a maximum size of M by M by M, there are exactly 2060 cuboids for which the shortest route has integer length when M=100, and this is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions is 1975 when M=99.
Find the least value of M such that the number of solutions first exceeds one million.

"""
def hasIntegerShortestRoute(size):
    a,b,c=size
    sqaurSum=[(a+b)**2+c**2,(b+c)**2+a**2,(c+a)**2+b**2]
    tmp={}
    for i in sqaurSum:
        tmp[i**0.5]=i
    t=min(tmp)
    if int(t)**2==tmp[t]: return True
    return False

def cuboidsNum(m,down=0):
    total=0
    for i in xrange(down+1,m+1):
        for j in xrange(1,i+1):
            for k in xrange(1,j+1):
                if hasIntegerShortestRoute((i,j,k)):
                    total+=1
    return total

def answer_very_slow():
    total=2060
    start=100
    while 1:
        total+=cuboidsNum(start+1,start)
        print start+1,total
        if total>1000000: break
        start+=1
    print total

def answer():
    L,c,a=1000000,0,2
    while c<L:
        a+=1
        for bc in xrange(3,2*a):
            if (bc*a)%12==0:
                s=(bc**2+a**2)**0.5
                if not s%1:
                    c+=min(bc,a+1)-(bc+1)//2
    print a

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 1818
# run time= 0.902395009995
