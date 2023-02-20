"""
Write a function which encrypts a plaintext using AES in ECB mode
Plaintext length: Multiple of 16 byte (16, 32, 48, etc.)
Use the Cryptography library
Generate the key in a proper manner (cf. Last lecture)
Takes key and plaintext as input, return ciphertext
"""
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

key = urandom(16)

pt = b"Hello Nice World"

cipher = Cipher(algorithms.AES(key), modes.ECB())

encryptor = cipher.encryptor()

ct = encryptor.update(pt) + encryptor.finalize()

"""
Write a function which decrypts a ciphertext using AES in ECB mode
Ciphertext length: Multiple of 16 bytes
Also use the Cryptography library
Takes key and ciphertext as input, return plaintext
"""

decryptor = cipher.decryptor()

dpt = decryptor.update(ct) + decryptor.finalize()

if dpt == pt:
    print("Correct")

"""
Check whether the encryption is correct
Must be able to decrypt what was encrypted, given key
"""