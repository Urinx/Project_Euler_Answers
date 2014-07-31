#!/usr/bin/env python
#coding:utf-8

"""
Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
-----------------------
| 131 673 234 103 18  |
| 201 96  342 965 150 |
| 630 803 746 422 111 |
| 537 699 497 121 956 |
| 805 732 524 37  331 |
-----------------------
Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

"""
def answer():
    with open('matrix.txt','r') as f:
        matrix=[]
        for i in f.readlines():
            tmp=i.replace('\r\n','').split(',')
            matrix.append([int(t) for t in  tmp])
        m,n=len(matrix),len(matrix[0])
        min_sum=[]
        [min_sum.append(n*[0]) for i in range(m)]

        Max=10e100
        for i in xrange(m):
            for j in xrange(n):
                if j==0: left=Max
                else: left=min_sum[i][j-1]
                if i==0: up=Max
                else: up=min_sum[i-1][j]
                if i+j==0: left=up=0
                min_sum[i][j]=matrix[i][j]+min(left,up)
        print min_sum.pop().pop()

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 427337
# run time= 0.0125269889832
