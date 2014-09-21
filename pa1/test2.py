"""
There are a lot of approaches to solve this. We define 2 xor functions: 1) xor of 2 hex strings -> list of int 2) xor of string (not hex) and list of int
"""

from ciphertext import ciphertext
import binascii


def hex_str2bytes(sh):
    return binascii.unhexlify(sh.encode())

def xor1(sh1, sh2):
    sb1 = hex_str2bytes(sh1)
    sb2 = hex_str2bytes(sh2)
    return [x ^ y for (x, y) in zip(sb1, sb2)]
    
def xor2(s, l):
    return "".join([chr(ord(x)^y) for (x,y) in zip(s, l)])


if __name__ == '__main__':
 
    ## this code is an example of crib-dragging
    for sh in ciphertext:
        s = 'Euler would probably enjoy that now his'
        l = xor1(sh, ciphertext[1])
        print(xor2(s, l))
