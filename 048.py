#!/usr/bin/env python
#coding:utf-8

"""

Self powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""

def anwser():
    print str(sum(map(lambda x:x**x,range(1,1001))))[-10:]

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 9110846700
# run time= 0.0236079692841