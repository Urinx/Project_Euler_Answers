#!/usr/bin/env python
#coding:utf-8

"""
Minimal network

The following undirected network consists of seven vertices and twelve edges with a total weight of 243.
The same network can be represented by the matrix below.
However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.
Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.

"""

def prim(G):
    # Prim Algorithm
    n=len(G)
    V=[]
    V_tmp=[]
    E=[]

    def updateV_tmp(V):
        V_tmp=[]
        for i in V:
            for j in range(n):
                if G[i][j]>0 and j not in V and j not in V_tmp:
                    V_tmp.append(j)
        return V_tmp
    
    def selectV(V,V_tmp):
        e_min=10e5
        e_v=(0,0)
        for v in V_tmp:
            for u in V:
                e=G[u][v]
                if e>0 and e<e_min:
                    e_min=e
                    e_v=(u,v)
        return e_v
    
    # init
    V.append(0)
    while len(V)<n:
        V_tmp=updateV_tmp(V)
        (u,v)=selectV(V,V_tmp)
        V.append(v)
        
        # for this problem I only save the weight of edge
        # E.append((u,v))
        E.append(G[u][v])
    
    return E

def answer():
    with open('p107_network.txt','r') as f:
        def a(i):
            if i=='-':
                return 0
            else:
                return int(i)
        G=[[a(i) for i in l.replace('\n','').split(',')] for l in f.readlines()]

        E=prim(G)
        saving=sum([sum(i) for i in G])/2-sum(E)
        print saving

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 259679
# run time= 0.0175929069519