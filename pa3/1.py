import hashlib
import binascii




# Read in the message from the input file
f = open("1.mp4", 'r+b')
s = f.read()
f.close()

print(len(binascii.hexlify(s[:100])))
print(len(s[:32]))


m = hashlib.sha256(s[:32])


print(m.digest().join(s[:32]))


