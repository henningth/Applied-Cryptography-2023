"""
Exercise 1: Starting from the first live-coding in module 3 (about MD5 and SHA1), 
add functionality so that the user can enter a string, which the program then 
computes and displays the MD5 and SHA1 hashes of. Test with strings that are 
similar, such as “Hello” and “H3llo”.
"""

from cryptography.hazmat.primitives import hashes

input_data1 = input("Enter a string:").encode()
input_data2 = input("Enter a string:").encode()

# MD-5 hash
def md5hash(input_data):
    md5_digest = hashes.Hash(hashes.MD5())
    md5_digest.update(input_data)
    md5_hash = md5_digest.finalize()
    print("MD5: " + md5_hash.hex())

# SHA-1 hash
def sha1hash(input_data):
    sha1_digest = hashes.Hash(hashes.SHA1())
    sha1_digest.update(input_data)
    sha1_hash = sha1_digest.finalize()
    print("SHA1: " + sha1_hash.hex())

md5hash(input_data1)
md5hash(input_data2)
sha1hash(input_data1)
sha1hash(input_data2)

"""
Exercise 2: Starting from the first live-coding in module 3 (about MD5 and SHA1), 
compute the MD5 and SHA1 hash of a file or your choosing. 
Have the program print the filename as well as the MD5 and SHA1 hashes of it. 
(Hint: To open a file in the same directory as the Python script, you can use:
filepath = os.path.dirname(__file__) + "\\" + filename
where filename is the name of the file.)
"""
import os
filename = "Dice.png"
filepath = os.path.dirname(__file__) + "\\" + filename

with open(filepath, "rb") as file:
    print("File:" + filename)
    data = file.read()
    md5hash(data)
    sha1hash(data)

import hashlib

filename = filepath

def file_as_bytes(file):
    with file:
        return file.read()

print("File is: "+filename)
print ("MD5: "+hashlib.md5(file_as_bytes(open(filename, 'rb'))).hexdigest())
print ("SHA1: "+hashlib.sha1(file_as_bytes(open(filename, 'rb'))).hexdigest())

"""
Exercise 3: Continuing from the previous exercise, 
download the two PDF files from https://shattered.io. 
Compute the SHA1 hash of each of the two files, what do you observe? 
What about the MD5 hashes of them?
"""
filename1 = "shattered-1.pdf"
filename2 = "shattered-2.pdf"

filepath1 = os.path.dirname(__file__) + "\\" + filename1
filepath2 = os.path.dirname(__file__) + "\\" + filename2

print("File is: "+filename1)
print ("MD5: "+hashlib.md5(file_as_bytes(open(filepath1, 'rb'))).hexdigest())
print ("SHA1: "+hashlib.sha1(file_as_bytes(open(filepath1, 'rb'))).hexdigest())

print("File is: "+filename2)
print ("MD5: "+hashlib.md5(file_as_bytes(open(filepath2, 'rb'))).hexdigest())
print ("SHA1: "+hashlib.sha1(file_as_bytes(open(filepath2, 'rb'))).hexdigest())
