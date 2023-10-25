from libnum import solve_crt, nroot

# test
N = [25777, 22879, 66277]
c1 = [19052, 4546, 44619]
c2 = [1708, 11733, 19731]
e = 3 

m1 = nroot(solve_crt(c1, N), 3)
m2 = nroot(solve_crt(c2, N), 3)

print(m1)
print(m2)