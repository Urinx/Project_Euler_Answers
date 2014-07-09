#!/usr/bin/env python
#coding:utf-8

"""
Cubic permutations

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.

"""
def code(num):
    s='0'*10
    l=list(str(num))
    for i in set(l):
        s=s[:int(i)]+str(l.count(i))+s[int(i)+1:]
    return s

def find_num(j,d):
    a=[]
    while 1:
        n=j**3
        if n/10**d>0:
            break
        a.append(n)
        j+=1
    b={}
    for i in a:
        flag=code(i)
        if flag in b:
            b[flag][1]+=1
        else:
            b[flag]=[i,1]

    for i in b:
        if b[i][1]==5:
            print b[i][0]
            j=-1
            break
    return j

def answer():
    j=346
    d=8
    while j:
        j=find_num(j,d)
        d+=1
        if j==-1: break

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 127035954683
# run time= 0.173566102982