import hashlib
import binascii
import math

# set block size
block_size = 1024


# read in the video file in binary
f = open("2.mp4", 'r+b')
s = f.read()
f.close()


# split s into 1024B blocks
if (len(s)%block_size == 0):
    number_blocks = len(s)/block_size
    size_last_block = block_size
else:
    number_blocks = math.floor(len(s)/1024)+1
    size_last_block = len(s) - (number_blocks - 1) * block_size


i = 0
hash_ob = hashlib.sha256(s[(len(s)-size_last_block):])
h = hash_ob.digest()


while i < number_blocks-1:

    current_block = s[(len(s)-size_last_block-block_size*(i+1)):(len(s)-size_last_block-block_size*i)]
    current_block_h = current_block + h

    # generate hash of current_block_h
    hash_ob = hashlib.sha256(current_block_h)
    h = hash_ob.digest()
    i += 1
    

print (binascii.hexlify(h))
