#!/usr/bin/env python
#coding:utf-8

"""

Lattice paths

Starting in the top left corner of a 2×2 grid, and only being 
able to move to the right and down, there are exactly 6 routes 
to the bottom right corner.
How many such routes are there through a 20×20 grid?

"""

def path1(x,y):
    if x==0 or y==0:
        return 1
    else:
        return path1(x,y-1)+path1(x-1,y)


p={}
def path2(x,y):
    if (x,y) not in p:
    	if x==0 or y==0:
    		l=1
    	else:
    		l=path2(x-1,y)+path2(x,y-1)
    	p[x,y]=p[y,x]=l
    return p[x,y]
    

def answer():
    print path2(20,20)

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# path2
# 137846528820
# run time= 0.000434160232544

# path1
# (10,10) run time= 0.0933589935303
# (14,14) run time= 15.1532649994
# (15,15) run time= 58.9713499546