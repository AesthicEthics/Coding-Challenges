"""
One of the simplest ways of coding a message is to do a letter shift.

For example, if you shift the letters in the original message by 5 then A in your original message becomes F in the coded message. 
(B → G, C → H, …, T → Y, U → Z, V → A, …, Z → E). To decode the message, you simply need to shift back by the same number.

A slightly trickier encryption uses a keyword to determine the amount of the shift. Suppose you were using a keyword ACT. To encode the message, you take the 
original message, remove everything but the alphabetic characters, and form the message into a block that has the same width as the keyword. Here is a sample 
message to encrypt:

BANANA & PEEL

The blocked version of the message is shown below with the keyword ACT as a header.

A	C	T
 		
B	A	N
A	N	A
P	E	E
L		
Now, the message is encoded using a letter shift. However, this time it is not a uniform shift, it will depend upon the keyword letter at the top of the column. 
If the letter at the top of the column is an A, then the letters in that column are not shifted. If the letter is a B, then the letter in that column shift by 1,
and so on. In the example, the letters in the third column will shift by 19 since the T is the 20th letter of the alphabet.

The encoded message is:

A	C	T
 		
B	C	G
A	P	T
P	G	X
L		
You will write a program that will accept a keyword and a string to be encoded. The keyword will never have more than 6 characters. The message will always be given in 
all upper case characters.

"""

from string import ascii_uppercase as alpha
import numpy as np
import re

def encode():
    letter = input("Type Header Here: ").upper()
    message0 = ((input(("Type Message Here: "))))
    message1 = (message0).replace(" ","")

    message = message1.upper()

    for char in '!@#$%^&*()-_=+/:;,.':
        message = message.replace(char,'')

    # all the lists
    lst = []
    lsta = []
    lstc = []
    var = []
    f = []
    listf = []

    #figuring out the length and the ranges

    a = len(letter)
    q = len(message)

    #loops for array and numeric conversion

    #getting all secret key into an array
    for i in range (0,a):
        lst.append(letter[i])

    #getting the alphabet into an array
    for i in alpha:
        lsta.append(i)

    #getting the actual message into an array
    for i in range(0,q):
        lstc.append(message[i])

    #print(lstc)

    #appending the alphabet index value for each of the letters in the secret code
    #into a seperate array to give us numeric value for shifts

    for i in range (0,a):
        var.append((lsta.index(lst[i])))

    #appending the alphabet index value for each letter in the message into a seper
    #erate array assigning them a numeric value

    for i in range (0,q):
        f.append(lsta.index(lstc[i]))

    n = len(f)

    #resizing arrays to allow for matrix addition
    ac = np.resize(var, n)

    #adding arays together
    trans = np.add(f,ac)

    final = len(trans)

    # 26 x 2 = 52 thus 52 is the max sum possible
    n2 = 52

    #re-sizing the alpabet array to repeat until it has 52 addresses
    a = np.resize(lsta, n2)

    for i in range (0,len(trans)):
        listf.append(a[(trans[i])])

    finalans = ''.join(map(str,listf))

    print(finalans)
    #for i in range(0,a):
        #shift =
    #print(lsta[5])
