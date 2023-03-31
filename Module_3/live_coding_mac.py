"""
Live coding: Message Authentication Codes
"""

from cryptography.hazmat.primitives import hashes, hmac
from os import urandom # For the key

key = urandom(16)
message = b'Yellow Submarine'
print("Key:" + str(key))
def computeTag(message, key):
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(message)
    tag = h.finalize()
    return tag

def verifyTag(message, key, tag):
    # Compute tag of input message
    computedTag = computeTag(message, key)
    # Compare the computed tag with the input tag
    if computedTag == tag:
        return True
    else:
        return False

computedTag = computeTag(message, key)
print(computedTag.hex())

result = verifyTag(message, key, computedTag)
print(result)