"""
Input: a, b (a > b)
Output: x, y, where ax + by = gcd(a, b)
"""
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = egcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

"""
Use extended Euclidean algorithm to calculate:
$a^{−1} \mod m$
Where $a \cdot a^{-1} \equiv 1 \mod m$
"""
def mod_inverse(a, m):
    if a < m:
        gcd, _, y = egcd(m, a)
    else:
        gcd, y, _ = egcd(a, m)
    if gcd != 1:
        raise ValueError("GCD isn't 1")
    else:
        return (y % m)


"""
Use Chinese Remainder Theorem to solve a system of congruences:
The system of r congruences $x \equiv a_i (\mod m_i), 1 \le i \le r$
has a unique solution modulo $M = m1 * m2...*m_r$, which is given by
$X = \sum_{i = 1}^{r} a_i\ M_i\ y_i (\mod M)$
Where $M_i = M/m_i and y_i = M_i^{-1}(\mod m_i), 1 \le i \le r$

Input: a[], m[], where m[i], m[j] are pair-wise relatively prime
"""
def solve_congruences_system(a, m):
    r = len(a)
    M = [0] * r
    y = [0] * r #inverse of M_i
    
    # M_prod: product of all moduli
    M_prod = 1
    for i in range(r):
        M_prod *= m[i]

    x = 0
    # Chinese Remainder Theorem
    for i in range(r):
        M[i] = M_prod // m[i]
        y[i] = mod_inverse(M[i], m[i])
        x += a[i] * M[i] * y[i]
    print("M: ", M_prod)
    print("M[]: ", M)
    print("y[]: ", y)
    print("X before mod: ", x)
    return (x % M_prod)

"""
Calculate keys
Input: p, q
Choose: e = 65537
Output: N, phi_N, d
pubkey: (N, e)
prikey: (N, d) 
"""
def calc_keys(p, q):
    N = p*q
    phi_N = (p-1)*(q-1)
    d = mod_inverse(e, phi_N)
    return N, phi_N, e, d

def char2num(char: str) -> int:
    return ord(char) - ord('a')

# Input: a block of 3 chars
def block2num(block: str) -> int:
    val = 0
    for i, char in enumerate(reversed(block)):
        val += char2num(char) * (26 ** i)
    return val

def str2blocks(s: str):
    blocks = [s[i:i+3] for i in range(0, len(s), 3)]
    num_blocks = [block2num(block) for block in blocks]
    n = len(num_blocks)
    return n, num_blocks

def RSA_enc(N, e, s):
    _, blocks = str2blocks(s)
    ciphertext = [(block ** e) % N for block in blocks]
    return ciphertext

# test

p = 139
q = 173
e = 7
N, phi_N, e, d = calc_keys(p, q)
print(f"When p={p}, q={q}. N={N}, phi_N={phi_N}, d={d}")
print(f"Public key: ({N}, {e})")
print(f"Private key: ({N}, {d})")
s = "cybersecurityisfun"
print("plaintext: ", s)
n, blocks = str2blocks(s)
print(f"n={n}, blocks={blocks}")  
ciphertext = RSA_enc(N, e, s)
print(f"ciphertext:\n{ciphertext}")  