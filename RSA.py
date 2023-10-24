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

"""
Input: p, q, d
Output: e
"""
def calc_e(p, q, d):
    phi_N = (p - 1) * (q - 1)
    for e in range(2, phi_N):
        if (e * d) % phi_N == 1:
            return e


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
"""
RSA encryption
input:PubKey (N, e), plaintext s is a string
output: cipertext, a list
"""
def RSA_enc(N, e, s):
    _, blocks = str2blocks(s)
    ciphertext = [(block ** e) % N for block in blocks]
    return ciphertext


def num2char(num: int) -> str:
    return chr(num + ord('a'))

# Input: a number in plaintext list
# Output: a string of 3 chars
def num2block(num: int) -> str:
    str_block = ""
    # MSB
    ch_high = num // (26 ** 2)
    str_block += num2char(ch_high)
    num -= ch_high * 26 ** 2

    ch_mid = num // 26
    str_block += num2char(ch_mid)
    num -= ch_mid * 26

    #LSB
    str_block += num2char(num)
    return str_block

"""
RSA decryption
m = c^d mod N
m - plaintext (a number)
c - ciphertext (a number)
pow(base, exponent, modulus)
input: PriKey (N, d), cipertext is a list
ouput: plaintex, a string
"""
def RSA_dec(N, d, ciphertext):
    m_list = []
    for c in ciphertext:
        m = pow(c, d, N)
        m_list.append(m)
    print("List of plaintext in number: ", m_list)

    plaintext = ""
    for m in m_list:
        plaintext += num2block(m)
    return plaintext

#return a list of all factors [1, n, p, q], p < q
def factoring(n):
    factors_list = []
    # 1 ~ sqrt(n)
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            factors_list.append(i)
            factors_list.append(n // i)
    return factors_list


# test

# encryption
print("----Run test for encryption----")
p = 139
q = 173
e = 7
s = "cybersecurityisfun"
print(f"Know: p={p}, q={q}, e={e}\nPlaintext:{s}")

N, phi_N, e, d = calc_keys(p, q)
print(f"When p={p}, q={q}. N={N}, phi_N={phi_N}, d={d}")
print(f"Public key: ({N}, {e})")
print(f"Private key: ({N}, {d})")
n, blocks = str2blocks(s)
print(f"n={n}, blocks={blocks}")
ciphertext = RSA_enc(N, e, s)
print(f"ciphertext:\n{ciphertext}")

# decryption
print("----Run test for decryption----")
ciphertext = [6340, 8309, 14010, 8936, 27358, 25023, 16481, 25809,
            23614, 7135, 24996, 30590, 27570, 26486, 30388, 9395,
            27584, 14999, 4517, 12146, 29421, 26439, 1606, 17881,
            25774, 7647, 23901, 7372, 25774, 18436, 12056, 13547,
            7908, 8635, 2149, 1908, 22076, 7372, 8686, 1304,
            4082, 11803, 5314, 107, 7359, 22470, 7372, 22827,
            15698, 30317, 4685, 14696, 30388, 8671, 29956, 15705,
            1417, 26905, 25809, 28347, 26277, 7897, 20240, 21519,
            12437, 1108, 27106, 18743, 24144, 10685, 25234, 30155,
            23005, 8267, 9917, 7994, 9694, 2149, 10042, 27705,
            15930, 29748, 8635, 23645, 11738, 24591, 20240, 27212,
            27486, 9741, 2149, 29329, 2149, 5501, 14015, 30155,
            18154, 22319, 27705, 20321, 23254, 13624, 3249, 5443,
            2149, 16975, 16087, 14600, 27705, 19386, 7325, 26277,
            19554, 23614, 7553, 4734, 8091, 23973, 14015, 107,
            3183, 17347, 25234, 4595, 21498, 6360, 19837, 8463,
            6000, 31280, 29413, 2066, 369, 23204, 8425, 7792,
            25973, 4477, 30989]
N = 31313
e = 4913
print(f"Know: N={N}, e={e}\nCiphertext: {ciphertext}")
factors_list = factoring(N)
p = factors_list[2]
q = factors_list[3]
_, _, _, d = calc_keys(p, q)
print(f"p:{p}, q:{q}, d:{d}")
plaintext = RSA_dec(N, d, ciphertext)
print("Plaintext: ", plaintext)
