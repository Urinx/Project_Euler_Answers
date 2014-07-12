#!/usr/bin/env python
#coding:utf-8

"""
Magic 5-gon ring

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.
Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.
It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
Total   Solution Set
9   4,2,3; 5,3,1; 6,1,2
9   4,3,2; 6,2,1; 5,1,3
10  2,3,5; 4,5,1; 6,1,3
10  2,5,3; 6,3,1; 4,1,5
11  1,4,6; 3,6,2; 5,2,4
11  1,6,4; 5,4,2; 3,2,6
12  1,5,6; 2,6,4; 3,4,5
12  1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.
Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?

"""
import itertools

def foo(a,b):
    s=''
    k=len(a)
    index=a.index(min(a))
    for i in xrange(index,index+k):
        s+=str(a[i%k])+str(b[i%k])+str(b[(i+1)%k])
    return int(s)

def answer():
    a=range(1,11)
    c=[]
    for i in itertools.permutations(a[:-1],5):
        b=set(a)^set(i)
        for j in itertools.permutations(b):
            if j[0]+i[0]+i[1]==j[1]+i[1]+i[2]==j[2]+i[2]+i[3]==j[3]+i[3]+i[4]==j[4]+i[4]+i[0]:
                c.append([j,i])
    d=[foo(i[0],i[1]) for i in c]
    print max(d)

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 6531031914842725
# run time= 0.711890935898