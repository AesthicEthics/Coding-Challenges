"""
Just a fun little peice of code that encode and decode messages and letter given a secret key
"""

import challenge2clean as clean
import challenge2rev as cleaner

print("Welcome To Engima!")

print("Would you like to encode or decode a message? ")
print("A) Encode")
print("B) Decode")

choice = input("Type Letter Here: ")

if choice == 'a':
    clean.encode()
else:
    cleaner.decode()
