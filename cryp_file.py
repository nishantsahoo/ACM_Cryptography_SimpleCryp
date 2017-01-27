import sys
from cryptography.fernet import Fernet
sys.stdout = open('Decrypt_file.txt', 'w')
# Put this somewhere safe!
a = {'A': '1',
     'B': '2',
     'C': '3',
     'D': '3',
     'E': '5', }

b = {}

key = Fernet.generate_key()
fer = Fernet(key)

for alpha, num in a.items():
    alpha_en = fer.encrypt(alpha)
    num_en = fer.encrypt(num)
    b.update({alpha_en: num_en})

for alpha, num in b.items():
    print fer.decrypt(alpha) + ':' + fer.decrypt(num)

sys.stdout = open('Encrypt_file.txt', 'w')

for alpha, num in b.items():
    print fer.decrypt(alpha) + ' : ' + fer.decrypt(num) + ' =',
    print alpha + ' : ' + num
