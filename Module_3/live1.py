from cryptography.hazmat.primitives import hashes

inputText = b'Yellow Submarine'

# MD5 hash
md5hash = hashes.Hash(hashes.MD5())
md5hash.update(inputText)
md5digest = md5hash.finalize()
print(md5digest.hex())

# SHA1 hash
sha1hash = hashes.Hash(hashes.SHA1())
sha1hash.update(inputText)
sha1digest = sha1hash.finalize()
print(sha1digest.hex())
