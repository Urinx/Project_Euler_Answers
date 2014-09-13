#!/usr/bin/env python
#coding:utf-8

"""
Anagramic squares

By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).
What is the largest square number formed by any member of such a pair?
NOTE: All anagrams formed must be contained in the given text file.

"""
import itertools

def check(n):
	m=int(n**0.5)
	if m**2==n: return True
	return False

def answer():
	with open('words.txt','r') as f:
		pair={}
		tmp={}
		words=f.read().replace('\"','').split(',')
		for w in words:
			t=tuple(sorted(set(w)))
			if t in tmp:
				tmp[t]+=[w]
			else: tmp[t]=[w]
		for i in tmp:
			l=len(tmp[i])
			if l>1:
				for j in range(l-1):
					for m in range(j+1,l):
						w1=tmp[i][j]
						w2=tmp[i][m]
						if sorted(w1)==sorted(w2):
							pair[w1,w2]=len(w1)
		pair=sorted(pair.items(),lambda x,y:cmp(y[1],x[1]))
		
		for (w1,w2),l in pair:
			m=0
			s=set(w1)
			k=len(s)
			for i in itertools.combinations('9876543210',k):
				for j in itertools.permutations(i,k):
					w4=w1
					for p in range(k):
						w4=w4.replace(list(s)[p],j[p])
					if w4[0]!='0':
						n1=int(''.join(w4))

						if check(n1):
							w3=w2
							for p in range(k):
								w3=w3.replace(list(s)[p],j[p])
							if w3[0]!='0':
								n2=int(''.join(w3))
								if check(n2):
									print n1,n2,w1,w2
									return

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 18769
# run time= 62.5653669834