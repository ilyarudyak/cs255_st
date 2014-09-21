from Crypto.Cipher import AES
import binascii

key = binascii.unhexlify('140b41b22a29beb4061bda66b6747e14')
ciphertext = binascii.unhexlify('5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253')
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
