# Exercise 4: Repeat the previous exercise but encode the string 
# in ASCII instead of UTF-8. Does it work? Why or why not?

userInput = input("Enter string: ")

userInputEncoded = userInput.encode('ASCII', 'replace')#, errors='strict')

print(userInputEncoded)