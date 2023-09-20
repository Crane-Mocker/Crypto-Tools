key_bin = bin(int("1F1F1F1F0E0E0E0E", 16))[2:].zfill(64)#put your K0 here 
print("Initial key (bin): ", key_bin)
print("len (bit): ", len(key_bin))

#Permutation Choice 1 (PC-1)
PC1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
K = "" #56-bit
for i in PC1:
	#print("i: ", i, " k: ", key_bin[i-1])
	K += key_bin[i-1]
print("56-bit K: ", K)
print("len (bit): ", len(K))

#Key Splitting
L0, R0 = K[:28], K[28:]
print("L0: ", L0)
print("R0: ", R0)

#shift_amount: 1 or 2, according to round_shifts[]
def circular_left_shift(bits,shift_amount):
	shiftedbits = bits[shift_amount:] + bits[:shift_amount]
	return shiftedbits

#k56: 56 bits key. k48: 48 bits key
def apply_PC2(pc2,k56):
	k48 = ""
	for index in pc2:
		k48 += k56[index-1]
	return k48

PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2, 41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
round_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
round_keys = list() 
for roundnumber in range(16):
	# key rotation
	newL = circular_left_shift(L0,round_shifts[roundnumber])
	newR = circular_left_shift(R0,round_shifts[roundnumber])
	# key compression (PC-2)
	roundkey = apply_PC2(PC2,newL+newR)
	round_keys.append(roundkey)
	L0 = newL
	R0 = newR

print(round_keys)
