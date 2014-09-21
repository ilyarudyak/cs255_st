from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii

key = binascii.unhexlify('36f18357be4dbd77f050515c73fcf9f2')
ciphertext = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'
ciphertext_hex = binascii.unhexlify(ciphertext)

## define length
length = 4

## generate blocks
c = []
i=32
while i < len(ciphertext):
    c.append(ciphertext[i:(i+32)])
    i += 32
c[3] = c[3] + '10000000'

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


    




