#!/usr/bin/env python
#coding:utf-8

"""

Power digit sum

2^15 = 32768 and the sum of its digits is 3+2+7+6+8=26.
What is the sum of the digits of the number 2^1000?

"""

def answer():
    print sum([int(i) for i in list(str(2**1000))])

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 1366