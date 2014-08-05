#!/usr/bin/env python
#coding:utf-8

"""
Counting rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

"""
def containRecNums(size):
    m,n=size
    if m==0 or n==0: return 0
    total=0
    for i in xrange(1,m+1):
        for j in xrange(1,n+1):
            total+=(n-j+1)*(m-i+1)
    return total

def answer():
    rectangles={}
    for i in xrange(100):
        for j in xrange(100):
            if (i,j) not in rectangles:
                t=containRecNums((i,j))
                rectangles[i,j]=rectangles[j,i]=abs(t-2000000)
            else:
                rectangles[j,i]=rectangles[i,j]
    area=min(rectangles,key=rectangles.get)
    print area[0]*area[1]

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 2772
# run time= 1.681224823