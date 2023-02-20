# Exercise 2: Write a Python program which 
# takes a positive integer as input and 
# prints the binary and hexadecimal representation of this integer

userDigit = input("Enter positive number: ")

for each in userDigit:
    print(str(each))
    print("bin: ", str(bin(int(each))))
    print("hex: ", str(hex(int(each))))

print(str(userDigit))
print("bin: ", str(bin(int(userDigit))))
print("hex: ", str(hex(int(userDigit))))