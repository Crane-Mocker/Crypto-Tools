"""
ElGamal
"""

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
ElGamal Decryption
d_k(y_1, y_2) = y_2(y_1^a)^{-1} (\mod p)
input: prikey a, ciphertext is a list [[y1, y2], []]
output: plaintext
"""
def ElGamal_dec(a, ciphertext):
    plaintext = []
    for y in ciphertext:
        y1_a = mod_inverse(y[0] ** a, p)# (y_1^a)^{-1}
        plaintext.append(y[1] * y1_a % p)
    print(plaintext)
    for elem in plaintext:
        print(num2block(elem), end="")

# test
p = 31847
alpha = 5
a = 7899
beta = 18074
print(f"p={p}, alpha={alpha}, a={a}, beta={beta}")
ciphertext = [[3781,14409], [31552,3930], [27214,15442], [5809,30274], 
            [5400,31486], [19936,721], [27765,29284], [29820,7710], 
            [31590,26470], [3781,14409], [15898,30844], [19048,12914], 
            [16160,3129], [301,17252], [24689,7776], [28856,15720], 
            [30555,24611], [20501,2922], [13659,5015], [5740,31233],
            [1616,14170], [4294,2307], [2320,29174], [3036,20132],
            [14130,22010], [25910,19663], [19557,10145], [18899,27609],
            [26004,25056], [5400,31486], [9526,3019], [12962,15189],
            [29538,5408], [3149,7400], [9396,3058], [27149,20535],
            [1777,8737], [26117,14251], [7129,18195], [25302,10248],
            [23258,3468], [26052,20545], [21958,5713], [346,31194],
            [8836,25898], [8794,17358], [1777,8737], [25038,12483],
            [10422,5552], [1777,8737], [3780,16360], [11685,133],
            [25115,10840], [14130,22010], [16081,16414], [28580,20845],
            [23418,22058], [24139,9580], [173,17075], [2016,18131],
            [19886,22344], [21600,25505], [27119,19921], [23312,16906],
            [21563,7891], [28250,21321], [28327,19237], [15313,28649],
            [24271,8480], [26592,25457], [9660,7939], [10267,20623],
            [30499,14423], [5839,24179], [12846,6598], [9284,27858],
            [24875,17641], [1777,8737], [18825,19671], [31306,11929],
            [3576,4630], [26664,27572], [27011,29164], [22763,8992],
            [3149,7400], [8951,29435], [2059,3977], [16258,30341],
            [21541,19004], [5865,29526], [10536,6941], [1777,8737],
            [17561,11884], [2209,6107], [10422,5552], [19371,21005],
            [26521,5803], [14884,14280], [4328,8635], [28250,21321],
            [28327,19237], [15313,28649]]
ElGamal_dec(a, ciphertext)