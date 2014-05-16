#!/usr/bin/env python
#coding:utf-8

"""

Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three,
four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used 
in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were 
written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 
(three hundred and forty-two) contains 23 letters and 115 
(one hundred and fifteen) contains 20 letters. The use of "and" 
when writing out numbers is in compliance with British usage.

"""

"""
one 3
two 4
three 5
four 4
five 4
six 3
seven 5
eight 5
nine 4
ten 3

eleven 6
twelve 6
thirteen 8
fourteen 8
fifteen 7
sixteen 7
seventeen 9
eighteen 8
nineteen 8

twenty 6 
thirty 6
forty 5
fifty 5
sixty 5
seventy 7
eighty 6
ninety 6

100 one hundred 3+7
101 one hundred and one
102 one hundred and two
103 one hundred and three
104 one hundred and four
105 one hundred and five
106 one hundred and six
107 one hundred and seven
108 one hundred and eight
109 one hundred and nine
120 one hundred and twenty
199 one hundred and ninety-nine
999 nine hundred and ninety-nine
1000 one thousand

"""

def anwser():
    a=[3,4,5,4,4,3,5,5,4,3]
    b=[6,6,8,8,7,7,9,8,8]
    c=[6,6,5,5,5,7,6,6]
    #1-99
    s1=sum(a)+sum(b)+sum(c)*10+sum(a[:9])*len(c)
    #100-999
    s2=sum(a[:9])*100+7*900+3*891+s1*9-190
    #1-1000
    s=s1+s2+11
    print s

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 21124