cipher_text = "" #put your ciphertext here

print("Cipher text: ", cipher_text)

for key in range(26):
	print("\nResult", key, ":", end="")
	for char in cipher_text:
		print(chr(((ord(char) - ord('A') - key) % 26) + ord('A')), end="")