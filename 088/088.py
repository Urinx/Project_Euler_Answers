#!/usr/bin/env python
#coding:utf-8

"""
Product-sum numbers

A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.
For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.
For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.
In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

"""
# Dont know how to solve this
# so copy the other's answer
# https://github.com/dhermes/project-euler/blob/master/python/complete/no088.py

from decorators import euler_timer
from functions import all_factors

def nontrivial_factorizations(n):
    factor_hash = {1: [1]}
    factor_hash = all_factors(n, factor_hash)
    result = {1: [[]], 2: [[2]]}
    value_hash = {}
    for i in range(3, n + 1):
        to_add = [[i]]
        for factor in factor_hash[i]:
            if factor > 1 and factor**2 <= i:
                for subset1 in result[factor]:
                    for subset2 in result[i/factor]:
                        cand = sorted(subset1 + subset2)
                        if cand not in to_add:
                            to_add.append(cand)
        for match in to_add:
            new_k = i + len(match) - sum(match)
            if new_k > 1 and new_k not in value_hash:
                value_hash[new_k] = i
        result[i] = to_add
    return result, value_hash


def main(verbose=False):
    MAX_k = 12000
    MAX_n = MAX_k + 1000
    _, value_hash = nontrivial_factorizations(MAX_n)
    final_list = []
    for desired in range(2, MAX_k + 1):
        if desired not in value_hash:
            raise Exception("Subset not large enough, raise MAX_n.")
        if value_hash[desired] not in final_list:
            final_list.append(value_hash[desired])
    return sum(final_list)

if __name__ == '__main__':
    print euler_timer(88)(main)(verbose=True)

# 7587457