mtime = int(input("Max Amount Of Time You Have: "))
chores = int(input("Number of Chores That Must Be Done: "))
b = []
for i in range(1,chores+1):
    a = int(input(f'Time to complete chore {i}: '))
    b.append(a)
c = sorted(b)
t = 0
for i in range(chores):
    t+=c[i]
    print(t)
    if t == mtime:
        print(i+1)
    elif t < mtime:
        print(i)
