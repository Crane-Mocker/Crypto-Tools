from math import gcd, sqrt
from z3 import *
import re

"""
Dixon's random squares method for factorization

Use SMT solver to set constraints 
and find the combination of b-smooth zs to construct perfect squares
"""

base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # -1 is the first

def is_b_smooth(z, n):
    e_vector = [0] * (len(base)+1) # exponent vector of one congurence
    e_vector[0], z_square = x_square_cong(z, n)
    for i in range(1, len(base)+1):
        while z_square % base[i-1] == 0:
            e_vector[i] += 1
            z_square //= base[i-1]
    
    if z_square == 1: # z^2 is b-smooth
        return True, e_vector
    else:
        return False, e_vector

def x_square_cong(z, n):
    if z * z > n:
        return 0, z * z % n
    else:
        return 1, abs(z*z % n - n)

def parse_mask(s):
    parsed_values = {}
    
    matches = re.findall(r'z(\d+) = (\d)', s)
    
    for match in matches:
        parsed_values[int(match[0])] = int(match[1])

    result = [parsed_values.get(i, 0) for i in range(max(parsed_values.keys())+1)]
    return result

def printFactors(mask, e_vectors, b_smooth_z):
    x_prod = 1
    y_prod = 1

    for i in range(len(mask)):
        if mask[i] == 1:
            # x
            x_prod *= b_smooth_z[i]
            # y
            e_vector = e_vectors[i]
            for j in range(1, len(e_vector)):
                y_prod *= base[j-1] ** e_vector[j]
    y_prod = int(sqrt(y_prod))
    if x_prod != y_prod and gcd(abs(x_prod + y_prod), n)!= 1:
        print(f"x:{x_prod}, y:{y_prod}")
        print(f"factors:{gcd(abs(x_prod - y_prod), n)},{gcd(x_prod + y_prod, n)}")

# Generate z3 constraints
# mask_i: whether the i-th b-smooth z is used
#         1 - used; 0 - not used
def genZ3Constraints(e_vectors):
    constraints = []
    length = len(e_vectors)
    length_base = len(base)+1

    for i in range(length):
        constraints.append(f"z{i} = Int(\'z{i}\')")

    constraints.append("s = Solver()")

    tmp_str = "("
    for i in range(length):
        constraints.append(f"s.add(z{i} <= 1, z{i} >= 0)")
        if i != length-1: #not the last
            tmp_str += f"z{i} + "
        else:
            tmp_str += f"z{i}) > 0"
    constraints.append(f"s.add({tmp_str})")

    for col in range(length_base):
        tmp_str = ""
        find_flag = 0
        for row in range(length):
            if e_vectors[row][col] != 0 and find_flag == 0:
                find_flag = 1
                tmp_str += f"{e_vectors[row][col]} * z{row}"
            elif e_vectors[row][col] != 0 and find_flag == 1:
                tmp_str += f"+ {e_vectors[row][col]} * z{row}"
        if tmp_str:
            constraints.append(f"s.add(({tmp_str}) %2  == 0)")
    constraints.append("s.check()")
    constraints.append("print(s.model())")
    constraints.append("mask = parse_mask(str(s.model()))")
    constraints.append("printFactors(mask, e_vectors, b_smooth_z)")
    return constraints

def genConstrainSolving(constraints):
    f = open("solve_constraints.py", "a")
    f.write("from z3 import *")
    f.write("from math import gcd, sqrt")
    for constraint in constraints:
        f.write(constraint)
    f.close()

def printConstraints(constraints):
    print("----z3 constraints----")
    for elem in constraints:
        print(elem)
    print("----------------------")

def dixon(n):
    factors = []
    b_smooth_z = [] # all z that is b-smooth
    e_vectors = []# all exponent vectors

    for z in range(500, 526):
        flag, e_vector = is_b_smooth(z, n)
        if flag:
            b_smooth_z.append(z)
            e_vectors.append(e_vector)
            print(f"b-smooth:{z}^2, e vector: {e_vector}")

    constraints = genZ3Constraints(e_vectors)
    #printConstraints(constraints)
    for constraint in constraints:
        exec(constraint)

# Test
n = 256961
dixon(n)
