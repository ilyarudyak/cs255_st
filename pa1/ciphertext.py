"""
read cipher strings from file to 
list ciphertext
"""

ciphertext = []
with open('ciphertext.txt') as f:
    for line in f:
        line = line.strip()
        if line != '' and line.find('ciphertext') == -1:
            ciphertext.append(line)

if __name__ == '__main__':
    print(ciphertext[0])
    print(ciphertext[len(ciphertext)-1])

