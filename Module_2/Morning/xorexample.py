# Compute XOR of A (pos. 65 i ASCII) and key 179

a = ord('A')
key = 179

# Encryption
ct = a ^ key

# Print ciphertext as ASCII character
ctASCII = chr(ct)

# Decryption
decrypted = ct ^ key

print(chr(decrypted))

# Print in binary
print("Key:  ", bin(key))
print("Ptxt: ", bin(a))
print("Ctxt: ", bin(ct))