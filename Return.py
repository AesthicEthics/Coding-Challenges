
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
