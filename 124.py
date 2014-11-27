#!/usr/bin/env python
#coding:utf-8

"""
Prime square remainders

Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn2.
For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.
The least value of n for which the remainder first exceeds 109 is 7037.
Find the least value of n for which the remainder first exceeds 1010.

"""

def answer():
    MAX =  100000+1

    factor_table = [1]*(1+MAX)  # largest factor, 1 means this number is prime
    def calculate_factors():
        i = 2
        while i <= (MAX/2):
            if factor_table[i] == 1:
                j = i*2
                while j <= MAX:
                    factor_table[j] = i
                    #print "factor_table[{0}] = {1}".format(j, i)
                    j += i
            i += 1

    print "Calculating factors with MAX={0}".format(MAX)
    calculate_factors()

    rad_table = []
    for n in range(1,MAX):
        nn = n
        factors = []
        prev_factor = n

        # Prime number
        if factor_table[nn] == 1:
            factors.append(nn)

        # Not a prime number
        while factor_table[nn] != 1:
            #print "    {0} is divisible by {1}".format(nn, factor_table[nn])
            if factor_table[nn] != prev_factor:
                factors.append(factor_table[nn])
                prev_factor = factor_table[nn]
            nn /= factor_table[nn]

        if nn != prev_factor:
            factors.append(nn)

        # Calculate rad(n)
        rad = 1
        for nn in factors:
            rad *= nn

        # Add to the list
        rad_table.append([rad, n])

    rad_table.sort()

    (rad, n) = rad_table[9999]
    print n

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 21417
# run time= 0.381587982178