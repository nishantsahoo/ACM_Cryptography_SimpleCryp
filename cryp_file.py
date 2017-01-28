import sys
from cryptography.fernet import Fernet
sys.stdout = open('Decrypt_file.txt', 'w')
# Put this somewhere safe!
a = {'A': '1',
     'B': '2',
     'C': '3',
     'D': '3',
     'E': '5', }

b = {}  # Empty dictionary

key = Fernet.generate_key()  # Generation of a fernet key
fer = Fernet(key)  # fernet object

# Encrypting items in 'a' and storing them in 'b'
for alpha, num in a.items():
    alpha_en = fer.encrypt(alpha)
    num_en = fer.encrypt(num)
    b.update({alpha_en: num_en})

# Decrypting items in 'b' and writing the values in the file Decrypt_file.txt
for alpha, num in b.items():
    print fer.decrypt(alpha) + ':' + fer.decrypt(num)

sys.stdout = open('Encrypt_file.txt', 'w')
# Writing encrypted values as well the decrypted values in the file Encrypt_file.txt
for alpha, num in b.items():
    print fer.decrypt(alpha) + ' : ' + fer.decrypt(num) + ' =',
    print alpha + ' : ' + num
