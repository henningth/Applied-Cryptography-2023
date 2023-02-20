# Define two bit strings 0b10110011 and 0b11011100

bitstring1 = int('10110011', 2)
bitstring2 = int('11011100', 2)

# The bitwise AND of the two bitstrings
bit1andbit2 = bitstring1 & bitstring2
print(bin(bit1andbit2))

# The bitwise OR of the two bitstrings
bit1andbit2 = bitstring1 | bitstring2
print(bin(bit1andbit2))

# The bitwise XOR of the two bitstrings (especially important!)
bit1andbit2 = bitstring1 ^ bitstring2
print(bin(bit1andbit2))

