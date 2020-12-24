a = int(input())
c = int(input())
b = int(input())
d = int(input())

if a == 1:
    q = 461
elif a == 2:
    q = 431
elif a == 3:
    q = 420
elif a == 4:
    q = 0

if b == 1:
    e = 130
elif b == 2:
    e = 160
elif b == 3:
    e = 118
elif b == 4:
    e = 0

if c == 1:
    f = 100
elif c == 2:
    f = 57
elif c == 3:
    f = 70
elif c == 4:
    f = 0

if d == 1:
    h = 167
elif d == 2:
    h = 266
elif d == 3:
    h = 75
elif d == 4:
    h = 0



print("Your total Calorie count is" + ' ' +  str((q)+(e)+(f)+(h)) +".")
