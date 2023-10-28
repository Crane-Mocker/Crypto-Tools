from math import sqrt, gcd

"""
Dixon's random squares method for factorization
"""

def dixon(n):
    base = [-1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    square_pairs = []

    # find x^2 \equiv y^2 (mod n)
    for x in range(int(sqrt(n)), n):
        for i in range(len(base)): # y's index
            x2 = x ** 2 % n # x^2
            y2 = base[i] ** 2 % n # y^2
            #print(f"x={x}, y={base[i]}")
            if x2 == y2:
                square_pairs.append([x, base[i]]) # [x, y]

    factors = []
    for i in range(len(square_pairs)):
        factor = gcd(square_pairs[i][0] - square_pairs[i][1], n)
        if factor != 1:
            factors.append(factor)

    return set(factors)

# test

n = 256961
factors = dixon(n)
print(factors)
