# Crypto-Tools

Crypto tools

## Shift Cipher: Exhaustive Key Search

`shift-ekey-search.py`

Exhaustive key search for Shift Cipher.

$\mathbb{C}=\mathbb{P}=\{A,B,...,Z\}$

## Vigenère: Friedman's Attack

`vigenere-friedman.py`

$\mathbb{C}=\mathbb{P}=\{A,B,...,Z\}$

Ref:
https://en.wikipedia.org/wiki/Letter_frequency
https://github.com/cbornstein/python-vigenere/blob/master/vigenere.py

## OTP: Encryption Matrix

`OTP-encryption-matrix.py`

$\mathbb{P} = \mathbb{C}$ $= \mathbb{K} $ $=(\mathbb{Z_{2}})^n$

$x=\{x_1,...,x_n\}$, $K=\{K_1,...,K_n\}$

$e_K(x)=x\ \oplus K$

$d_K(y)=y\ \oplus K$

## DES: Round Key Schedule

`DES-key.py`

## AES128: Round Key Schedule

`AES128-key.py`

## RSA

`egcd()` extended euclidean algorithm

Input: a, b (a > b)
Output: x, y, where ax + by = gcd(a, b)

`solve_congruences_system()`

Use Chinese Remainder Theorem to solve a system of congruences:
The system of r congruences $x \equiv a_i (\mod m_i), 1 \le i \le r$
has a unique solution modulo $M = m1 * m2...*m_r$, which is given by
$X = \sum_{i = 1}^{r} a_i\ M_i\ y_i (\mod M)$
Where $M_i = M/m_i$ and $y_i = M_i^{-1}(\mod m_i), 1 \le i \le r$

Input: a[], m[], where m[i], m[j] are pair-wise relatively prime

`calc_keys()`

Calculate keys
Input: p, q
Choose: e = 65537
Output: N, phi_N, d
pubkey: (N, e)
prikey: (N, d) 

**RSA Key generation algorithm (original):**

- Generate 2 large random primes, p and q, of approximately equal size such that their product n=pq is of the required bit length
- Compute N=pq and $\phi(N)$ =(p−1)(q−1)
- Choose an integer e, $1 \lt e \lt \phi(N)$, such that gcd(e, $\phi(N)$) = 1
- Compute the secret exponent d, $1 \lt d \lt \phi(N)$, such that $ed \equiv 1 \mod \phi(N)$
- The public key is (N, e) and the private key is (d, p, q). Private key also can be written as (N, d)

e can be chosen from 3,5,17,257,65537

**Encryption**

Input: pubkey + plaintext

$c = m^e \mod N$

m - plaintext (int)
c - ciphertext (int)

**Decryption**

Input: prikey + ciphertext

$m = c^d \mod N$

## Pollard’s Rho Algorithm

for factorization

## Dixon's Random Squares Method

for factorization