
import gmpy2, math
from gmpy2 import mpz, isqrt, is_power, mul



a = 1
b = 1
c = -6


D = isqrt(mpz(b**2-4*a*c))
x1 = mpz((-b+D)/(2*a))
x2 = mpz((-b-D)/(2*a))

print(x1, x2, a*x1**2+b*x1+c, a*x2**2+b*x2+c)
