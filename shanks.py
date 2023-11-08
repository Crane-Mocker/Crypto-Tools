from math import ceil, sqrt
"""
Shanks baby step giant step
Find x, such a^x \equiv b (mod p)
-> x = log_a b
p should be prime
"""
def shanks(a, b, p):
    n = ceil(sqrt(p-1))
    # baby step
    table = {pow(a, i, p): i for i in range(n)}
    c = pow(a, n*(p-2), p)
    # giant step
    for i in range(n):
        y = (b * pow(c, i, p)) % p
        if y in table:
            return i*n + table[y]
    return None

# test
# log_{106}12375 in Z_{24691}*
print(shanks(106, 12375, 24691))
# log_6 248388 in Z_{458009}*
print(shanks(6, 248388, 458009))

