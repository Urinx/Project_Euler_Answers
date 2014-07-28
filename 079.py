#!/usr/bin/env python
#coding:utf-8

"""
Passcode derivation

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
The text file, keylog.txt, contains fifty successful login attempts.
Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

"""
def answer():
	with open('keylog.txt','r') as f:
		passwd=[i.replace('\r\n','') for i in f.readlines()]
		a,b,c=[],[],[]
		for i in passwd:
			a+=[i[0]]
			b+=[i[1]]
			c+=[i[2]]
		print 'Start to crack the password...'
		l=len(set(b))+2
		print 'The length of password is:',l
		pw=l*['']
		pw[0]=list(set(a)^(set(a)&set(b)))[0]
		pw[-2]=list(set(b)^(set(a)&set(b)))[0]
		pw[-1]=list(set(c)^(set(b)&set(c)))[0]
		pw[1]=list(set(b)^(set(b)&set(c)))[0]
		
		p4=set(c)&(set(a)&set(b))
		for p in passwd:
			if set(p) < p4:
				print p
		print 'So the password could be:'
		print ''.join(pw[:2])+'1682'+''.join(pw[-2:])
		print ''.join(pw[:2])+'1628'+''.join(pw[-2:])

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 73162890
# run time= 0.000575065612793