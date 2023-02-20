# Exercise 1: Write a Python program which takes a 
# string as input, and prints the individual byte 
# values of the string

string = input("Enter string: ")

output = []

for x in string:
    output.append(ord(x))

print(output)

#for i in range(len(string)):
#    print(string[i])

for i in string:
    print("'" + i + "'" + str(bin(ord(i.encode('UTF-8')))))
    #print("'" + i + "'" + str(bin(i.encode('UTF-8')))) # Virker ikke