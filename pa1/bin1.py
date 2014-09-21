"""
We have 10 messages encrypted with time-pad. c = m xor key.
And we need to decrypt them (and other - 11 secret message).

The idea is to do: 1) c' = c1 xor c5 = m1 xor m5 and then 2) c' xor 'There '.We guess that c5 starts with 'The'. We will get first 6 symbols of m1 - 'We can'. Why? c' xor 'There ' = m1 ([:7], due to a xor a = 0). And then we repeat with different string - see the code in main().

This is crib-dragging - see http://crypto.stackexchange.com/questions/2249/how-does-one-attack-a-two-time-pad-i-e-one-time-pad-with-key-reuse
"""
from ciphertext import ciphertext
import binascii

def hex2str_bin(sh):
    """
    replace hex codes for characters using chr
    '616263ff' -> 'abc\xff'
    """

    # encode '61' -> b'61'
    sh = sh.encode()

    # unhexlify b'61' -> b'a'
    sh = binascii.unhexlify(sh)

    # convert to string using chr and return
    return "".join([chr(x) for x in sh])



def strxor(a, b):
    """
    xor two strings of different lengths (up to min of their len)
    character by character using ord and then translate 
    back to string using chr. so we can have non ascii symbols
    """
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])





if __name__ == '__main__':

    ## this code is an example of crib-dragging
    for sh in ciphertext:
        
        
        str1 = strxor(hex2str_bin(sh), hex2str_bin(ciphertext[1]))
        str2 = 'Euler would probably enjoy that now his'
        print(strxor(str1, str2))




