"""
Problem: 

You have been asked by a parental unit to do your chores.

Each chore takes a certain amount of time, but you may not have enough time to do all of your chores, since you can only complete one chore at a time. 
You can do the chores in any order that you wish.

What is the largest amount of chores you can complete in the given amount of time?

"""


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
