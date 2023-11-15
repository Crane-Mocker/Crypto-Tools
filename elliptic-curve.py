from sympy import mod_inverse

"""
Elliptic-curve: y^2 = x^3 + ax + b mod p
"""

def is_quadratic_residue(n, p):
    return pow(n, (p - 1) // 2, p) == 1

# all points on curve
def find_points_on_curve(a, b, p):
    points = []
    for x in range(p):
        y_squared = (x**3 + a*x + b) % p
        if is_quadratic_residue(y_squared, p):
            # Find the square root of y_squared modulo p
            for y in range(p):
                if (y * y) % p == y_squared:
                    points.append((x, y))
                    if y != 0:
                        points.append((x, p - y))
                    break
    return points

# Let y = 0, find roots
def find_roots(a, b, p):
    roots = []
    for x in range(p):
        if (x ** 3 + a*x + b) % p == 0:
            roots.append(x)
    return roots


def point_negate(P, p):
    return (P[0], -P[1] % p)

# double a point
def point_double_mod(x1, y1, a, b, p):
    if y1 == 0:
        return 'infinity'  # Point at infinity

    lambda_val = (3 * x1**2 + a) * mod_inverse(2 * y1, p) % p
    x3 = (lambda_val**2 - 2 * x1) % p
    y3 = (lambda_val * (x1 - x3) - y1) % p
    return x3, y3

# add 2 points
def point_add_mod(x1, y1, x2, y2, a, b, p):
    if x1 == x2 and y1 != y2:
        return 'infinity'  # Point at infinity

    if x1 != x2:
        lambda_val = (y2 - y1) * mod_inverse(x2 - x1, p) % p
    else:
        # point doubling
        return point_double_mod(x1, y1, a, b, p)

    x3 = (lambda_val**2 - x1 - x2) % p
    y3 = (lambda_val * (x1 - x3) - y1) % p
    return x3, y3

# print all multiples of a point P
def calculate_multiples_of_point(P, a, b, p, max_multiple):
    current = P
    multiples = []

    for i in range(1, max_multiple + 1):
        if i == 1:
            multiples.append(P)
        else:
            current = point_add_mod(current[0], current[1], P[0], P[1], a, b, p)
            if current == 'infinity':
                break
            multiples.append(current)

    return multiples

# print nP. n can be positive or negative
def calculate_multiple_of_point(P, a, b, p, n):
    if n == 0:
        return 'infinity'  # nP is the point at infinity
    elif n < 0:
        P = point_negate(P, p)
        n = -n

    result = P
    for _ in range(n - 1):
        result = point_add_mod(result[0], result[1], P[0], P[1], a, b, p)
        if result == 'infinity':
            break

    return result

def num2chr(num):
    print(chr(num - 1 + ord('A')), end="")

def point_decompress(x, parity, a, b, p):
    y_squared = (x**3 + a*x + b) % p
    for potential_y in range(p):
        if (potential_y * potential_y) % p == y_squared and potential_y % 2 == parity:
            return (x, potential_y)
    return None

"""
m: private key
P: point
Q: mP
"""
def simple_elliptic_curve_dec(ciphertexts, m, P, Q, a, b, p):
    plaintexts = []
    for ciphertext in ciphertexts:
        y1, y2 = ciphertext
        # (x0, y0) = m * Point-Decompress(y1)
        decompressed_y1 = point_decompress(y1[0], y1[1], a, b, p)
        if decompressed_y1 is None:
            return None

        x0, y0 = calculate_multiple_of_point(decompressed_y1, a, b, p, m)

        plaintext = (y2 * mod_inverse(x0, p)) % p
        plaintexts.append(plaintext)
    return plaintexts

# test

print("----Points----")
a = 1
b = 28
p = 71
print(f"Find all points on curve y^2 = x^3 + {a}x + {b} mod {p}")
points_on_curve = find_points_on_curve(a, b, p)
print(points_on_curve)
print("Let y=0, roots are: ", find_roots(a, b, p))
print("When x=0, it is a point at infinity")

a = 1
b = 26
p = 127
P = (11, 15)
print("Calculate following points on curve y^2 = x^3 + {a}x + {b} mod {p}")
print("(9, 16) + (6, 11) =" , point_add_mod(9, 16, 6, 11, a, b, p))
print("-(11, 15) =", calculate_multiple_of_point(P, a, b, p, -1))
print("2(4, 27) =", point_double_mod(4, 27, a, b, p))

print("----Decryption----")
a = 41
b = 83
p = 179
P = (9, 110) 
m = 16 #pri key
Q = calculate_multiple_of_point(P, a, b, p, m) #pub key
print(f"For curve y^2 = x^3 + {a}x + {b} mod {p}")
print(f"Q=mP={m}*{P}={Q}")
ciphertexts = [((91, 0), 148),((106, 0), 153),((78, 0), 111),((137, 0), 21),((29, 1), 81),((151, 1), 5),((115, 1), 149)]
plaintexts = simple_elliptic_curve_dec(ciphertexts, m, P, Q, a, b, p)
print("plaintexts: ", plaintexts)
for plaintext in plaintexts:
    num2chr(plaintext)
print("\n")


