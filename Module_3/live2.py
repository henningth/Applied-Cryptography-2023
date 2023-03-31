"""
Write a program in Python which computes the MAC of some given 
data and a secret key
Use HMAC in the Cryptography module

Write it as a function computeTag(m,k), which returns the tag
Add a function verifyTag(m, t, k) which takes message m, 
tag t and key k as input, and returns True or False 
depending on whether tag is valid (=not tampered with)
"""

from cryptography.hazmat.primitives import hmac, hashes
from cryptography.exceptions import InvalidSignature
import os

def computeTag(m, k):
    hash = hmac.HMAC(k, hashes.SHA256())
    hash.update(m)
    tag = hash.finalize()
    return tag

def verifyTag(m, t, k):
    computedTag = computeTag(m, k)
    if t == computedTag:
        print("OK.")
    else:
        print("FAIL.")
    """
    try:
        hash.verify(t)
        print("OK.")
    except InvalidSignature:
        print("ERROR.")
    """

inputText = b'Yellow Submarine'
key = os.urandom(16)

tag1 = computeTag(inputText, key)
print(tag1.hex())

inputText2 = b'Yellow submarine'
verifyTag(inputText, tag1, key)