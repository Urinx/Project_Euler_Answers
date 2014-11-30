#!/usr/bin/python

import os
from math import sqrt, factorial
from functools import reduce

def factor(n):
    if n in [-1, 0, 1]: return []
    if n < 0: n = -n
    F = []
    while n != 1:
        p = trial_division(n)
        e = 1
        n /= p
        while n%p == 0:
            e += 1; n /= p
        F.append((p,e))
    F.sort()
    return F

def sos_digits(n): #sum of squares of the digits of an integer by Po
  s=0
  while n:
    s+=(n%10)**2
    n=n//10
  return s

def open_data_file(filename):
    f = open(os.path.join(os.path.dirname(__file__), "data", filename))
    return f


def memoize(func):
    memo = {}
    def wrapper(*args):
        if args in memo:
            return memo[args]
        memo[args] = result = func(*args)
        return result
    return wrapper


def is_prime(n):
    """Determine whether a number is prime using trial division"""

    if n < 2:
        return False
    if (n == 2 or n == 3 or n == 5 or n == 7 or n == 11 or n == 13 or
            n == 17 or n == 19 or n == 23 or n == 29):
        return True
    if not (n % 2 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and
            n % 17 and n % 19 and n % 23 and n % 29):
        return False

    # all primes are of the form c#k + i for i < c# and i coprime to c#
    # let c = 6, c# = 2*3*5 = 30

    max_divisor = int(sqrt(n))
    divisor = 30

    while divisor <= max_divisor:
        if not (n % (divisor + 1) and n % (divisor + 7) and n % (divisor + 11) and
                n % (divisor + 13) and n % (divisor + 17) and n % (divisor + 19) and
                n % (divisor + 23) and n % (divisor + 29)):
            return False
        divisor += 30

    return True


def prime_sieve(n):
    """Return all prime numbers <= n. Implements The Sieve of Eratosthenes"""

    if n <= 1:
        return []

    bound = (n-1) // 2 # last index of the sieve
    sieve = [True]*(bound+1)

    for i in range(1, int(sqrt(n)//2)+1):
        if sieve[i]: # 2*i+1 is a prime, mark multiples
            for j in range(2*i*(i+1), bound+1, 2*i+1):
                sieve[j] = False
    primes = [2]
    for i in range(1, bound+1):
        if sieve[i]:
            primes.append(2*i+1)
    return primes


# http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf
def prime_sieve_lazy():
    yield 2
    n = 3
    composites = {}

    while True:
        if n not in composites:
            yield n
            composites[n*n] = [n]
        else:
            for prime in composites[n]:
                composites.setdefault(prime*2 + n, []).append(prime)
            del composites[n]
        n += 2


def prime_factors(n, primes=None):
    """Return prime factors of an integer. 'primes' should be None or a list
    of primes up to sqrt(n)"""

    if primes is None:
        primes = prime_sieve(int(sqrt(n)))

    factors = []

    for prime in primes:
        if prime*prime > n:
            break

        if n % prime == 0:
            n //= prime
            exponent = 1
            while n % prime == 0:
                n //= prime
                exponent += 1
            factors.append((prime, exponent))
    if n > 1:
        factors.append((n, 1))

    return factors

def sum_of_divisors(n, primes=None):
    if n == 1:
        return 1
    # http://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors
    return reduce(lambda x,y: x * (y[0]**(y[1]+1)-1)//(y[0]-1), prime_factors(n, primes), 1)

def sum_of_proper_divisors(n, primes=None):
    return sum_of_divisors(n, primes) - n

# returns the Greatest Common Divisor of a and b (Euclidean algorithm)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# checks if a number is palindromic in the given base
def is_palindrome(n, base):
    r = 0
    t = n
    while t > 0:
        r = r * base + t % base
        t //= base
    return r == n

def is_palindromic(n):
    return n == int(str(n)[::-1])

# checks if a number is x to y pandigital
# the function doesn't check for redundant digits
def is_pandigital(n, end=9, start=1):
    res = 0

    while n > 0:
        res |= (1 << n % 10)
        n //= 10

    return res == (2**(end-start+1) - 1) << start

# checks if an integer is a permutation of another
def is_permutation(a, b):
    if (a - b) % 9: # the difference must be a multiple of 9.
        return False
    return sorted(str(a)) == sorted(str(b))


# functions for calculating polygonal numbers
def nth_triangle(n):
    return n*(n+1)//2

def nth_square(n):
    return n*n

def nth_pentagonal(n):
    return n*(3*n - 1)//2

def nth_hexagonal(n):
    return n*(2*n-1)

def nth_heptagonal(n):
    return n*(5*n-3)//2

def nth_octagonal(n):
    return n*(3*n - 2)


def is_pentagonal(n):
    k = (sqrt(24*n+1)+1)/6
    return k.is_integer()

# returns Pythagorean triplets with a+b+c=p using the formula a+b+c = 2*m*(m+n)*d
# p is always even
# http://projecteuler.net/overview=009
def pythagorean_triplets(p):
    p >>= 1

    for m in range(2, int(sqrt(p)+1)):
        if p % m == 0:
            pm = p // m
            while not pm&1: # reduce the search space by removing all factors 2
                pm >>= 1
            k = m + 2 if m&1 else m + 1

            while k < 2*m and k <= pm:
                if pm % k == 0 and gcd(k, m) == 1:
                    d = p//(k*m)
                    n = k - m
                    a = d*(m*m - n*n)
                    b = 2*d*m*n
                    c = d*(m*m + n*n)
                    yield (a, b, c)
                k += 2

# returns the number of k-combinations of a set of n elements
def number_of_combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

# returns continued fraction expansion of a square root, e.g. sqrt(6) -> [2, 2, 4]
# http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
def sqrt_fraction_expansion(num):
    m = 0
    d = 1
    a0 = a = int(sqrt(num))

    expansion = [a0]

    while a != 2*a0:
        m = d*a - m
        d = (num - m*m)//d
        a = (a0 + m)//d
        expansion.append(a)

    return expansion

# get convergent fractions resulting from the quotients
# http://en.wikipedia.org/wiki/Continued_fraction#Continued_fraction_expansions_of_.CF.80
def convergent_fractions(quotients):
    num, den, prev_num, prev_den = next(quotients), 1, 1, 0

    while True:
        yield num, den
        q = next(quotients)
        prev_num, num, prev_den, den = num, prev_num + num*q, den, prev_den + den*q

# Copyright (c) 2010 the authors listed at the following URL, and/or
# the authors of referenced articles or incorporated external code:
# http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)?action=history&offset=20101013093632
def miller_rabin_pass(a, s, d, n):
  a_to_power = pow(a, d, n)
  if a_to_power == 1:
    return True
  for i in range(s-1):
    if a_to_power == n - 1:
      return True
    a_to_power = (a_to_power * a_to_power) % n
  return a_to_power == n - 1
 
def miller_rabin(n):
  d = n - 1
  s = 0
  while d % 2 == 0:
    d >>= 1
    s += 1
  for repeat in range(20):
    a = 0
    while a == 0:
      a = random.randrange(n)
    if not miller_rabin_pass(a, s, d, n):
      return False
  return True

def trial_division(n, bound=None):
    if n == 1: return 1
    for p in [2, 3, 5]:
        if n%p == 0: return p
    if bound == None: bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7; i = 1
    while m <= bound and m*m <= n:
        if n%m == 0:
            return m
        m += dif[i%8]
        i += 1
    return n

#! usr/bin/python

# All the Binomial related functions by Hector

import math as m

def binomial(n, k):
    """
    Returns the binomial cofficiend(n, k) for positive 'n' and 'k'.
    It generaltes fast binomial coefficeint with the following formula

        C(n, k) = prod of{ (n - (k -i))/i } for i = 1 to k
    """
    if k > n - k: # take advantage of symmetry
        k = n - k
    c = 1
    for i in range(k):
        c = c * (n - i)
        c = c / (i + 1)
    return c


def binomial_app(n, k):
    """
    Returns the approximate Binomial coefficient of large 'n' and 'k'
    Using the following formula - 

    T == Gamma function
    
        C(n, k) = exp( ln(T(n + 1)) - ln(T(k+1)) - ln(T(n - k + 1)) )

    And ln(T(z)) can be calculated as - 
        ln(T(z)) = (z - 1/2) * ln(z) - z + ln(2 * pi)/2 
    """
    if c < 10000:
        return binomial_coefficient(n, k)

    ln_T_n1 = (n + 1/2.) * m.log(n + 1) - (n + 1) + m.log(2 * m.pi)/2.
    ln_T_k1 = (k + 1/2.) * m.log(k + 1) - (k + 1) + m.log(2 * m.pi)/2.
    ln_T_nk1 = ( n - k + 1/2.) * m.log( n - k + 1)  - (n - k + 1) + m.log(2 * m.pi)/2.

    pw = ln_T_n1 - ln_T_k1 - ln_T_nk1 
    if  pw < 700:
        return m.exp(pw)
    else:
        return "exp(%d)"%pw

def expt_mul(a, b):
    r = 1
    for i in xrange(b):
        r *= a
    return r

def expt_rec(a, b):
    if b == 0:
        return 1
    elif b % 2 == 1:
        return a * expt_rec(a, b - 1)
    else:
        p = expt_rec(a, b / 2)
        return p * p

def expt_bin_rl(a, b):
    r = 1
    while 1:
        if b % 2 == 1:
            r *= a
        b /= 2
        if b == 0:
            break
        a *= a

    return r

def _bits_of_n(n):
    """ Return the list of the bits in the binary
        representation of n, from LSB to MSB
    """
    bits = []

    while n:
        bits.append(n % 2)
        n /= 2

    return bits

