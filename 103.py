#!/usr/bin/env python
#coding:utf-8

"""
Special subset sums: optimum

Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:
S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special sum sets are given below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.
By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.
Given that A is an optimum special sum set for n = 7, find its set string.
NOTE: This problem is related to Problem 105 and Problem 106.

"""
import itertools

def check(s):
	# If B contains more elements than C then S(B)>S(C)
	k=2
	while k<=len(s)/2+1:
		if sum(s[:k])<=sum(s[-k+1:]):
			return False
		k+=1
	# S(B)≠S(C)
	for i in xrange(2,len(s)-1):
		tmp=[]
		for j in itertools.combinations(s,i):
			t=sum(j)
			if t in tmp:
				return False
			else:
				tmp.append(t)
	return True

def A(n):
	if n==1: return [1]
	else:
		a=A(n-1)
		b=a[len(a)/2]
		return optimum([b]+[b+i for i in a])

def optimum(a):
	if len(a)<6: return a
	b=a[0]
	s=sum(a)

	param=[[i+j for j in range(-3,4)] for i in a[1:]]
	for i in itertools.product(*param):
		t=[b]+list(i)
		if all(map(lambda x,y:x<y and x*y>0,t[1:-1],t[2:])) and sum(t)<s:
			if check(t):
				return t
	return a

def answer():
	print reduce(lambda x,y:str(x)+str(y),A(7))

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 20313839404245
# run time= 0.333258152008