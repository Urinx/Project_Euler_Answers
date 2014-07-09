#!/usr/bin/env python
#coding:utf-8
import math

"""

Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 
3124 is one possible permutation of the digits 1, 2, 3 and 4. If 
all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations 
of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 
1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

def answer():
	# 9!=362880    ==>  2xxxx xxxxx
	# 8!=40320     ==>  27xxx xxxxx
    a=range(10)
    num=''
    n=1000000
    for x in xrange(9,0,-1):
    	f=math.factorial(x)
    	m,n=n/f,n%f

    	if n==0:
    		num+=str(a[m-1])
    		del a[m-1]
    		num+=''.join(map(lambda x:str(x),a[::-1]))
    		break

    	num+=str(a[m])
    	del a[m]

    print num

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 2783915460
# run time= 8.51154327393e-05