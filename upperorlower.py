a = (input())
x = 0
y = 00
for i in a:
    if i.islower():
        x+=1
    elif i.isupper():
        y+=1
if y > x:
    print(a.upper())
elif y == x:
    print(a)
else:
    print(a.lower())
