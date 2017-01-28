import random
import sys
sys.stdout = open('Random_Key_dictionary.txt', 'w')
indices = list(range(0, 26))
dict = {}  # empty dictionary

# Assigning random indices to the alphabets
for i in range(0, 26):
    key = random.choice(indices)
    dict.update({chr(i+97): key})
    indices.remove(key)

print 'Key values: '
for alpha, key in dict.items():
    print alpha + ' : ' + str(key)

print
message = "secret"
encrypt = ""

# Encryption of the original message
for each in message:
    for alpha, key in dict.items():
        if each == alpha:
            en_key = chr(key+97)
            encrypt += en_key

print 'Original message: ' + message
print 'Encrypted message: ' + encrypt

decrypt = ""
for each in encrypt:
    for alpha, key in dict.items():
        if each == chr(key+97):
            de_key = alpha
            decrypt += de_key

print 'Decrypted message: ' + decrypt
