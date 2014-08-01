#!/usr/bin/env python
#coding:utf-8

"""
Path sum: three ways

NOTE: This problem is a more challenging version of Problem 81.
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.
-----------------------
| 131 673 234 103 18  |
| 201 96  342 965 150 |
| 630 803 746 422 111 |
| 537 699 497 121 956 |
| 805 732 524 37  331 |
-----------------------
Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.

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

        '''
        # Greedy
        Max=10e100
        min_sum=[Max,0,0]
        pre=[0,0,0]
        for i in xrange(m):
            tmp=matrix[i][1]+matrix[i][0]
            if tmp<min_sum[0]: min_sum=[tmp,i,1]
        while 1:
            m_s,i,j=min_sum
            if j==n-1: break
            if i==0: up=[Max,-1,-1]
            else: up=[m_s+matrix[i-1][j],i-1,j]
            if i==m: down=[Max,-1,-1]
            else: down=[m_s+matrix[i+1][j],i+1,j]
            right=[m_s+matrix[i][j+1],i,j+1]
            now=[up,down,right]
            for p in range(3):
                if pre[1:]==now[p][1:]: now[p][0]=Max
            pre=min_sum
            min_sum=min(now)
        print min_sum
        # 477004
        '''

        def findmin(i,j):
            left=min_sum[i][j-1]
            pathsum=[left]
            upsum=0
            for up in xrange(i-1,-1,-1):
                upsum+=matrix[up][j]
                if upsum>left: break
                pathsum+=[upsum+min_sum[up][j-1]]
            downsum=0
            for down in xrange(i+1,m):
                downsum+=matrix[down][j]
                if downsum>left: break
                pathsum+=[downsum+min_sum[down][j-1]]
            return matrix[i][j]+min(pathsum)

        for i in xrange(m):
            min_sum[i][0]=matrix[i][0]
        for j in xrange(1,n):
            for i in xrange(m):
                min_sum[i][j]=findmin(i,j)
        print min([min_sum[i][-1] for i in range(m)])

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 260324
# run time= 0.135611057281
