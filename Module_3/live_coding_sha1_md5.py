"""
Compute SHA-1 and MD-5 of a bytearray of our own choice.
"""

from cryptography.hazmat.primitives import hashes

input_data = b'Yellow Submarine'

# MD-5 hash
md5_digest = hashes.Hash(hashes.MD5())
md5_digest.update(input_data)
md5_hash = md5_digest.finalize()
print(md5_hash.hex())

# SHA-1 hash
sha1_digest = hashes.Hash(hashes.SHA1())
sha1_digest.update(input_data)
sha1_hash = sha1_digest.finalize()
print(sha1_hash.hex())