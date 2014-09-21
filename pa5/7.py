import gmpy2
from gmpy2 import mpz



p = 997
h = 535
g = 7
B = 35


x0, x1 = 0, 0


d = {}
for i in range(B):
    d[gmpy2.divm(h, pow(g,i), p)] = i

print(d)


test = 0
flag = True
for i in range(B):
    test = pow(g, gmpy2.mul(B, i), p)

    # search in hash table
    if test in d:
        x0, x1, flag = i, d[test], False
        break
    if flag == False: break
    

print(x0, x0*B + x1)
