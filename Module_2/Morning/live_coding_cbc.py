"""
Write a Python program which can encrypt and decrypt using AES in CBC mode
Plaintext length: Multiple of 16 bytes
"""
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

def encrypt(key, iv, plaintext):
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(iv))
    encryptor = cipher.encryptor() # Set cipher to encrypt
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

def decrypt(key, iv, ciphertext):
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(iv))
    decryptor = cipher.decryptor() # Set cipher to decrypt
    decryptedtext = decryptor.update(ciphertext) + decryptor.finalize()
    return decryptedtext

key = urandom(16)
iv = urandom(16)

plaintext = b'Hello AES World!'
ciphertext = encrypt(key, iv, plaintext)

decryptedtext = decrypt(key, iv, ciphertext)

if plaintext == decryptedtext:
    print("Correct")
else:
    print("Failed")