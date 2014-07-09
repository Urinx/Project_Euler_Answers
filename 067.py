#!/usr/bin/env python
#coding:utf-8

"""
Maximum path sum II

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

"""
a=open('triangle.txt','r').read()
b=[]
for i in a.split('\n')[:-1]:
    b.append([int(j) for j in i.split(' ')])
c=[[i,i] for i in b[-1]]

def answer():
    for i in xrange(len(b)-2,-1,-1):
        for j in xrange(0,i+1):
            if c[j][-1]<=c[j+1][-1]:
                c[j]=c[j+1][:]
            c[j].append(c[j][-1]+b[i][j])
            c[j][-2]=b[i][j]
        c.pop()
    print 'Sum is',c[0].pop()

def draw():
    temp=c[0][-1::-1]
    print '='*45
    for i in a.split('\n'):
        t=c[0].pop()
        print i.replace(str(t),'\033[31m%d\033[0m' % t)
    print '='*45
    print '->'.join([str(i) for i in temp])

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 7273
# run time= 0.00915908813477