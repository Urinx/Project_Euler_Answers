#!/usr/bin/env python
#coding:utf-8

"""
Path sum: four ways

NOTE: This problem is a more challenging version of Problem 81.
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.
-----------------------
| 131 673 234 103 18  |
| 201 96  342 965 150 |
| 630 803 746 422 111 |
| 537 699 497 121 956 |
| 805 732 524 37  331 |
-----------------------
Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.

"""
def answer():
    with open('matrix.txt','r') as f:
        matrix={}
        m,n=0,0
        for i in f.readlines():
            tmp=i.replace('\r\n','').split(',')
            for t in tmp:
                matrix[m,n]=int(t)
                n+=1
            m+=1
            n=0

        def neighbor(u):
            i,j=u
            v=[(i-1,j),(i,j+1),(i+1,j),(i,j-1)]
            return v

        def dijkstra(graph,start,end):
            Q={}
            for g in graph: Q[g]=float('inf')
            Q[start]=graph[start]
            dist={}
            while 1:
                u=min(Q,key=Q.get)
                dist[u]=Q[u]
                del Q[u]
                if u==end: break
                for v in neighbor(u):
                    if v in Q:
                        tmp=dist[u]+graph[v]
                        if Q[v]>tmp: Q[v]=tmp
            return dist

        min_sum=dijkstra(matrix,(0,0),(79,79))
        print min_sum[79,79]

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 425185
# run time= 3.45563101768
