"""
Jane's family has just moved to a new city and today is her first day of school. She has a list of instructions for walking from her home to the school. 
Each instruction describes a turn she must make. For example, the list

Copy
R
QUEEN
R
FOURTH
R
SCHOOL

means that she must turn right onto Queen Street, then turn right onto Fourth Street, then finally turn right into the school. Your task is to write a computer program 
which will create instructions for walking in the opposite direction: from her school to her home.

The input and output for your program will be formatted like the samples below. You may assume that Jane's list contains at least two but at most five instructions,
and you may assume that each line contains at most 10 characters, all of them capital letters. The last instruction will always be a turn into the SCHOOL.
"""
a = []
c = []
for i in range(0,11):
    b = str(input())
    a.append(b)
    if b == "SCHOOL":
        break
a.remove('SCHOOL')
for i in range(0,len(a)):
    if a[i] == "R":
        d = "LEFT"
    elif a[i] == "L":
        d = "RIGHT"
    else:
        d = a[i]
    c.append(d)
f = c[::-1]
f.append('HOME')
for i in range(0,(len(f))):
    x = f[i]
    if x == "LEFT" or x == "RIGHT":
        if f[i+1] == "HOME":
            print(f'Turn {x} into your {f[i+1]}.')
        else:
            print(f'Turn {x} onto {f[i+1]} street.')
