
import gmpy2
from gmpy2 import mpz, isqrt, is_power, mul

N1 = "6484558428080716696628242653467722787263437207069762630604390703787" \
    "9730861808111646271401527606141756919558732184025452065542490671989" \
    "2428844841839353281972988531310511738648965962582821502504990264452" \
    "1008852816733037111422964210278402893076574586452336833570778346897" \
    "15838646088239640236866252211790085787877"

N = mpz(int(N1))
x = 0

for A in range(isqrt(N), isqrt(N) + 2**20):

    if is_power(mul(A,A) - N) == True:
        x = isqrt(mul(A,A) - N)
        break

print(A-x)
