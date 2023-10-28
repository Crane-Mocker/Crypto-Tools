from math import gcd, sqrt
from itertools import chain, combinations

"""
Dixon's random squares method for factorization
"""

base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def is_b_smooth(z, n):
    z_square = x_square_cong(z, n)
    e_vector = [0] * len(base) # exponent vector of one congurence
    for i in range(len(base)):
        while z_square % base[i] == 0:
            e_vector[i] += 1
            z_square //= base[i]
    
    if z_square == 1: # z^2 is b-smooth
        return True, e_vector
    else:
        return False, e_vector

def x_square_cong(z, n):
    if z * z > n:
        return z * z % n
    else:
        return abs(z*z % n - n)

def powset(set):
    s = list(set)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def printCombinations(masks, e_sums):
    print(f"{len(masks)} combinations found.")
    for i in range(len(masks)):
        print(f"mask:{masks[i]}, e vector:{e_sums[i]}")

def dixon(n):
    factors = []
    b_smooth_z = [] # all z that is b-smooth
    e_vectors = []# all exponent vectors

    for z in range(500, 526):
        flag, e_vector = is_b_smooth(z, n)
        if flag:
            b_smooth_z.append(z)
            e_vectors.append(e_vector)
            print(f"b-smooth:{z}^2, e vector: {e_vector}")

    # to get every possible combination of exponent vectors
    # find powerset for the set of all exponent vectors
    powset_e_vectors = powset(e_vectors) # powset_e_vectors[0] is empty set

    # for each subset, find a mask
    # mask[j] = 1 -> the z_j is used
    masks = []
    e_sums = []
    for i in range(1, len(powset_e_vectors)):
        mask = [0] * len(b_smooth_z)
        e_sum = [0] * len(base) # sum of exponents at same position
        for vector in powset_e_vectors[i]:
            mask[e_vectors.index(vector)] = 1
            for j in range(len(vector)):
                e_sum[j] += vector[j]
        
        findPerfectSquare = True
        for j in range(len(base)):
            if e_sum[j] % 2 != 0:
                findPerfectSquare = False
        if findPerfectSquare: # perfect square constructed
            masks.append(mask)
            e_sums.append(e_sum)

    #printCombinations(masks, e_sums)

    # check gcd for each pair of x, y (perfect square) constructed
    for i in range(len(masks)):
        mask = masks[i]
        e_sum = e_sums[i]
        x_prod = 1
        y_prod = 1

        for j in range(len(mask)):
            if mask[j] == 1:
                x_prod *= b_smooth_z[j]

        for j in range(len(e_sum)):
            if e_sum[j] != 0:
                y_prod *= base[j] ** (e_sum[j] // 2)

        print(f"mask:{mask}, a:{e_sum}")
        print(f"x product:{x_prod}, y product:{y_prod}")

        if x_prod != y_prod and gcd(abs(x_prod + y_prod), n)!= 1:
            factors.append(gcd(abs(x_prod + y_prod), n))
            factors.append(gcd(abs(x_prod - y_prod), n))

    return set(factors)

# Test

n = 256961
factors = dixon(n)
print("factors: ", factors)

