


p = 997
h = 550

## find generator
gen = 0
for g in range (1,p):
    
    Zp = []
    for j in range (1,p):
        tmp = pow(g,j,p)
        if not(tmp in Zp): Zp.append(tmp)


    if len(Zp) == p - 1:
        gen = g
        break

print ("gen =", gen, len(Zp))           

## find DLog(h) with base g: h = g^x
log = 0
for x in range (1,p):
    if pow(gen, x, p) == h:
        log = x
        break

print("x = " + str(log), "g^x % p - h = " + str(pow(gen, log, p) - h))
