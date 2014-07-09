#!/usr/bin/env python
#coding:utf-8

"""

Counting Sundays

You are given the following information, but you may prefer to 
do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not 
  on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the 
twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

month={0:31,1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def is_leap_yeay(year):
	if year%400==0:
		return True
	if year%4==0 and year%100!=0:
		return True
	return False

def answer():
	total,sundays=365-31,0
	for y in xrange(1901,2001):
		if is_leap_yeay(y):
			month[2]=29
		else:
			month[2]=28
		for m in xrange(1,13):
			total+=month[m-1]
			if (total+1)%7==0:
				sundays+=1
	print sundays

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 171
# run time= 0.000494003295898