import string
from time import time

"""
Construct decryption table for RSA
"""

def genPlaintext():
    strings = []
    for c1 in string.ascii_lowercase:
        for c2 in string.ascii_lowercase:
            for c3 in string.ascii_lowercase:
                strings.append(c1+c2+c3)
    return strings
        

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

# create a ciphertext list according to the plaintext
def genCiphertextList(N, e, plaintext):
    ciphertext = []
    for s in plaintext:
        #ctime = time()
        ciphertext.append(RSA_enc(N, e, s))
        #print("time for one enc: ", time() - ctime)
    return ciphertext

# Test

e = 65537
N = 27695331379663144618774919824948294735508562097315627474064780394616856602327810697077924719234095544759088657891979773374203255850501992735432341329006941764992659223811450982270505832262910573969878155667808305545986768167619808573208672742829657463110298739995622710664428599151335974480959220016496922039999127186483656573835688036822168077181318900816480327020900780842826320901895397938617969378699197967183865653506229401010293795794562102112159999604170316040188908218150419089805829057110122779490134523539214990248129351455721442589027414339623068545791933648949393486253909386966167196603064382471223938999

plaintext = genPlaintext()
print("Plaintext generate.")

ciphertext = genCiphertextList(N, e, plaintext)
print("Decryption table constructed.")

f = open('RSA-dec-table.txt', 'a') 
for i in range(len(plaintext)):
    f.write(str(plaintext[i]))
    f.write(str(ciphertext[i]))
    f.write("\n")
f.close()
print("Decryption table saved at RSA-dec-table.txt.")
