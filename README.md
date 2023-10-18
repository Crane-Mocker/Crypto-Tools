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