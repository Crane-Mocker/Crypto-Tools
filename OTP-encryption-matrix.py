n = 4 #put your n here

matrix = []

header_row = ["x/K"] + [format(K, f'0{n}b') for K in range(2**n)]
matrix.append(header_row)

for x in range(2**n):
    row = [format(x, f'0{n}b')]
    for K in range(2**n):
        ciphertext = x ^ K
        row.append(format(ciphertext, f'0{n}b'))
    matrix.append(row)

for row in matrix:
    print(" | ".join(row))
