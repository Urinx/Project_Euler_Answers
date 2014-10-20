#!/usr/bin/env python
#coding:utf-8

"""
Diophantine reciprocals II

In the following equation x, y, and n are positive integers.
1/x+1/y=1/n
It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for which the total number of distinct solutions exceeds one hundred.
What is the least value of n for which the number of distinct solutions exceeds four million?
NOTE: This problem is a much more difficult version of Problem 108 and as it is well beyond the limitations of a brute force approach it requires a clever implementation.

"""

def Twos(limit,exponents):
    exponents[0]=0
    divisors=1

    for e in exponents:
        divisors*=2*e+1

    exponents[0]=(limit/divisors-1)/2

    while divisors*(2*exponents[0]+1)<limit:
        exponents[0]+=1

    return exponents

def Number(prime,exponents):
    number=reduce(lambda x,y:x*y,map(lambda x,y:x**y,prime,exponents))
    return number

def SetAllSmallerExponents(exp,exponents):
    for i in range(exp):
        exponents[i]=exponents[exp]
    return exponents

def answer():
    prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43]
    exponents=[0]*len(prime)

    result=reduce(lambda x,y:x*y,prime)
    limit=2*4000000-1
    counter=1

    while 1:
        exponents=Twos(limit,exponents)

        if exponents[0]<exponents[1]:
            counter+=1
        else:
            number=Number(prime,exponents)
            if number<result: result=number
            counter=1

        if counter>=len(exponents): break

        exponents[counter]+=1
        exponents=SetAllSmallerExponents(counter,exponents)

    print result


import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 9350130049860600
# run time= 1.19770789146