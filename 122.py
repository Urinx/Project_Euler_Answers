#!/usr/bin/env python
#coding:utf-8

"""
Efficient exponentiation

The most naive way of computing n15 requires fourteen multiplications:
n × n × ... × n = n15
But using a "binary" method you can compute it in six multiplications:
n × n = n2
n2 × n2 = n4
n4 × n4 = n8
n8 × n4 = n12
n12 × n2 = n14
n14 × n = n15
However it is yet possible to compute it in only five multiplications:
n × n = n2
n2 × n = n3
n3 × n3 = n6
n6 × n6 = n12
n12 × n3 = n15
We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.
For 1 ≤ k ≤ 200, find ∑ m(k).

"""
from Queue import PriorityQueue as pq

def answer():
	items = pq()
	items.put( (0,-1,{1}) )
	SIZE = 200
	vals = [3000] * (SIZE+1)
	vals[0] = 0

	while 3000 in vals:
		item = items.get()
		priority = item[0]
		new_priority = priority+1
		old_val = -1*item[1] # reason for making it negative is due to
		elem = item[2]      #implementation of priority queue. Takes smallest first.
		
		if old_val > SIZE:
			continue

		if vals[old_val] > priority:
			vals[old_val] = priority

		for i in elem:
			new_val = i+old_val
			if new_val > SIZE or vals[new_val] != 3000:
				continue
			new_set = set(list(elem))
			new_set.add(new_val)
			items.put( (new_priority,-1*new_val,new_set) )

	print sum(vals)

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 1582
# run time= 0.347441911697