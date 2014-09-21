from Crypto.Cipher import AES
import binascii

key = binascii.unhexlify('140b41b22a29beb4061bda66b6747e14')
ciphertext = binascii.unhexlify('4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81')
ciphertext1 = ciphertext[16:32]
ciphertext2 = ciphertext[32:48]
ciphertext3 = ciphertext[48:64]

iv = ciphertext[:16]

                                
aes = AES.new(key, AES.MODE_CBC, iv)
plaintext1 = aes.decrypt(ciphertext1)
plaintext2 = aes.decrypt(ciphertext2)
plaintext3 = aes.decrypt(ciphertext3)

print(plaintext1 + plaintext2 + plaintext3)
print(len(ciphertext1), len(ciphertext1), len(ciphertext1))
