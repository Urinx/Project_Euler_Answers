#!/usr/bin/env python
#coding:utf-8

"""
How many reversible numbers are there below one-billion

Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits.
For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible.
Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.
How many reversible numbers are there below one-billion (10^9)?
"""

def reversible_numbers(limit):
    limit = int(limit)
    amount = 0
    for x in xrange(limit):
        sx = str(x)
        if x % 100000 == 0: print(x / 1e9)
        if sx[-1] != '0' and (int(sx[0]) + int(sx[-1])) % 2 != 0:
            y = x + int(sx[::-1])
            if all([int(d) % 2 for d in str(y)]):
                amount += 1
    print(amount)

reversible_numbers(1e9)
# 