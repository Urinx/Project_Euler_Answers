#!/usr/bin/env python
#coding:utf-8

"""
Special subset sums: testing

Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:
S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations and S(A) = 1286.
Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing seven to twelve elements (the two examples given above are the first two sets in the file), identify all the special sum sets, A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).

NOTE: This problem is related to Problem 103 and Problem 106.

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

def answer():
	t=0
	with open('p105_sets.txt','r') as f:
		sets=[sorted([int(j) for j in i.replace('\n','').split(',')]) for i in f.readlines()]
		for s in sets:
			if check(s):
				t+=sum(s)
	print t

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 73702
# run time= 0.137167930603