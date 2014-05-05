#!/usr/bin/env python

"""

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""

def anwser_1():
    sum=0
    for x in xrange(3,1000):
        if x%3==0 or x%5==0:
            sum+=x
    print sum

def anwser_2():
    def a(j,k):
        return j*(k*(k+1))/2
    sum_3=a(3,1000/3)
    sum_5=a(5,1000/5-1)
    sum_15=a(15,1000/15)
    print sum_3+sum_5-sum_15

anwser_1()
anwser_2()

# Anwser:233168
