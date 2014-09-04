#!/usr/bin/env python
#coding:utf-8

"""
Roman numerals

The rules for writing Roman numerals allow for many ways of writing each number (see About Roman Numerals...). However, there is always a "best" way of writing a particular number.
For example, the following represent all of the legitimate ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least number of numerals.
The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; that is, they are arranged in descending units and obey the subtractive pair rule (see About Roman Numerals... for the definitive rules for this problem).
Find the number of characters saved by writing each of these in their minimal form.
Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

"""
import re

def answer():
    with open('roman.txt','r') as f:
        roman=f.read()
        print len(roman)-len(re.sub('DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII', '  ', roman))

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 743
# run time= 0.00199699401855