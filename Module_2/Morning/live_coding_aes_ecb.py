"""
Write a function which encrypts a plaintext using AES in ECB mode
Plaintext length: Multiple of 16 byte (16, 32, 48, etc.)
Use the Cryptography library
Generate the key in a proper manner (cf. Last lecture)
Takes key and plaintext as input, return ciphertext
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

def encrypt(key, plaintext):
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

key = urandom(16) # Generate key
plaintext = b'Hello AES World!Hello AES World!'
ciphertext = encrypt(key, plaintext)
print(ciphertext)

"""
Write a function which decrypts a ciphertext using AES in ECB mode
Ciphertext length: Multiple of 16 bytes
Also use the Cryptography library
Takes key and ciphertext as input, return plaintext
"""
def decrypt(key, ciphertext):
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB())
    decryptor = cipher.decryptor()
    decryptedtext = decryptor.update(ciphertext) + decryptor.finalize()
    return decryptedtext

decryptedtext = decrypt(key, ciphertext)
print(decryptedtext)