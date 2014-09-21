import gmpy2, time
from gmpy2 import mpz, powmod, mul, t_mod



p = mpz(13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171)
g = mpz(11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568)
h = mpz(3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333)
B = mpz(2**20)

gB = powmod(g,B,p)
g_inv = gmpy2.invert(powmod(g,1,p), p)
x0, x1 = 0, 0
d = {}

start1 = time.clock()
for i in range(B):
    tmp = t_mod(mul(h ,powmod(g_inv,i,p)), p)
    d[tmp] = i
##    d[gmpy2.divm(h, pow(g,i,p), p)] = i

elapsed1 = (time.clock() - start1)


test = 0

start2 = time.clock()
for i in range(B):
    test = powmod(gB, i, p)

    # search in hash table
    if test in d:
        x0, x1 = i, d[test]
        break
    if i == 100: print("2")
elapsed2 = (time.clock() - start2)    

print(x0, x0*B + x1)
print(elapsed1, elapsed2)
