import random
from math import gcd
"""
Pollard's Rho Algorithm for prime factoring
Input: n
output: d - divisor, i - iterations
"""

def PollardRho(n):
    # n's divisor is itself
    if n == 1:
        return n, 0

    # an even number has 2 as a prime divisor
    if n % 2 == 0:
        return 2, 0

    # constant c
    #c = random.randint(2, n-1)
    c = 1
    x = 2 #T
    y = 2 #H
    f = lambda x: x**2 + c
    d = 1

    i = 0
    while d == 1:
        x = f(x) % n
        y = f(f(y)) % n
        d = gcd((x -y ) % n, n)
        i += 1
    if d != n:
        return d, i

# test
n_list = [262063, 9420457, 181937053]
for n in n_list:
    d, i = PollardRho(n)
    print(f"n={n}, d={d}, i={i}")