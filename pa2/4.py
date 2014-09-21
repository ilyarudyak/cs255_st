from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii

key = binascii.unhexlify('36f18357be4dbd77f050515c73fcf9f2')
ciphertext = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'

print(len(ciphertext))

## define length
length = 2

## generate blocks
c = []
i=32
while i < len(ciphertext):
    c.append(ciphertext[i:(i+32)])
    i += 32
c[1] += '1000'

## generate aes
aes = AES.new(key)

## generate iv
iv = []
iv0 = int(ciphertext[:32],16)
for i in range(length):
    iv.append(binascii.unhexlify( (hex(iv0+i))[2:34] ) )

## encrypt (iv+i) with key
e = []
for i in range(length):
    tmp = aes.encrypt(iv[i])
    e.append(binascii.hexlify(tmp))

## generate result
result = []
for k in range(length):
    i = 0
    
    while i < 32:
        result.append(int(c[k][i:(i+2)], 16)^int(e[k][i:(i+2)], 16))
        i += 2

msg = []
for r in result:
    msg.append(chr(r))

print(''.join(msg))


    










