from collections import Counter
import itertools

ciphertext=""#put your ciphertext here
key_len_max=10# put your possible max key length here. integer

freq = {
    'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 'F': 0.02228, 'G': 0.02015, 'H': 0.06094,
    'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507, 'P': 0.01929,
    'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056, 'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150,
    'Y': 0.01974, 'Z': 0.00074
}

def getChar(num):
    return chr(num + ord('A'))

def getNum(c):
    return ord(c) - ord('A')

def getKeyLetter(c):
    return getChar((min(c, key=lambda k: c[k])))

def getSq(s):
    exp_count = dict.fromkeys(range(26), 0)
    chiSq = 0
    for y in range(26):
        exp_count[y]=freq[getChar(y)]*len(s)

    for y in range(26):
            chiSq= chiSq+(((s.count(getChar(y))-exp_count[y])**2)/exp_count[y])

    return chiSq

def countChar(text):
    char_count = {}
    
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def calculate_ic(text):
    n = len(text)
    letter_count = [0] * 26
    total = 0

    for char in text:
        if 'A' <= char <= 'Z':
            letter_count[ord(char) - ord('A')] += 1
            total += 1

    ic = sum((count / total) * ((count - 1) / (total - 1)) for count in letter_count)
    return ic

def estimate_key_length(ciphertext):
    max_key_length = min(key_len_max, len(ciphertext))
    ic_values = []

    for length in range(1, max_key_length + 1):
        subtexts = [''] * length
        for i, char in enumerate(ciphertext):
            subtexts[i % length] += char

        ic_sum = 0
        for subtext in subtexts:
            ic_sum += calculate_ic(subtext)

        average_ic = ic_sum / length
        ic_values.append(average_ic)

    estimated_key_length = ic_values.index(max(ic_values)) + 1
    #print("IC:")
    #print(ic_values)
    return estimated_key_length

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            char_num = ord(char.upper()) - ord('A')
            key_char = key[i % key_length].upper()
            key_num = ord(key_char) - ord('A')
            decrypted_char_num = (char_num - key_num) % 26
            decrypted_char = chr(decrypted_char_num + ord('A'))
            if char.islower():
                decrypted_char = decrypted_char.lower()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

def find_Key(key_length, ciphertext, freq):
    keys = [''] * key_length
    for j in range(key_length):
        for i in range(j, len(ciphertext), key_length):
            keys[j] += ciphertext[i]

    masterDictionary = {}
    for i in range(key_length):
        masterDictionary['d'+str(i)] = dict.fromkeys(range(26), '')

    for x in range(key_length):
        for j in range(26):
            for i in keys[x]:
                masterDictionary['d'+str(x)][j] = masterDictionary['d'+str(x)][j]+getChar(((getNum(i))-j)%26)

    #Perform Chi Square analysis on the deciphered strings and store in masterCipher
    masterCipher = {}
    for i in range(key_length):
        masterCipher['c'+str(i)] = dict.fromkeys(range(26), '')

    for i in range(key_length):
        for j in range(26):
            masterCipher['c'+str(i)][j] = getSq(masterDictionary['d'+str(i)][j])

    key = ''
    for i in range(key_length):
        key = key + getKeyLetter(masterCipher['c'+str(i)])

    return key

key_length = estimate_key_length(ciphertext)
print("Guessed key len: ", key_length)

key = find_Key(key_length, ciphertext, freq)
print("Guessed Key:", key)

plaintext = vigenere_decrypt(ciphertext, key)
print("plaintext: ", plaintext)