"""
qwertytown4life is getting bullied for using Python 3. Help cheer him up by creating a program that tells him the alphabet score of a word.

A word's alphabet score is the occurrence of each letter times the place that letter is in the alphabet. For example, the string ab gives 3 because there is one a, 
and it is the first letter in the alphabet. So a's alphabet score 1×1=1. Next, there is one b, and because b is the second letter in the alphabet, b's alphabet score 
is 1×2=2. Therefore the string's alphabet score is 1+2=3.

Also, you must code it in Python 3.
"""
a = list((input()))
e = []
c = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(a)):
    d = (c.index(a[i]) + 1)
    e.append(d)
print(sum(e))
