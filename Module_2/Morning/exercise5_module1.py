# Exercise 5: Write a Python program that opens a 
# PNG file in binary mode and prints the 
# first 8 bytes of the file (its signature). 
# Compare with https://en.wikipedia.org/wiki/Portable_Network_Graphics#File_header 

file = open("pngfile.png", "rb")

file_content = file.read(8)

file.close()

print(file_content)

with open("pngfile.png", mode="rb") as file:
    file.seek(0,0) # Sikker på at vi starter i begyndelsen af filen
    openfile = file.read(8)
    
