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
