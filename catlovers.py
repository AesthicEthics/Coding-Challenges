"""
Kirito loves cats. He joined a survey with N people and a single question:

Do you like cats more or dogs more? You may only choose one.

All N people are required to answer. Each person answered with cats or dogs.

If someone responds with cats, then he or she likes cats more. Otherwise, he or she likes dogs more.

Given that all N people answered with either cats or dogs, what was the total preference?

Note: If the number of responses for cats and dogs are equal, then output equal.
"""
a = int(input())
d =[]
for i in range(0,a):
    c = input()
    d.append(c)
x = 0
xx = 0
for i in range(len(d)):
    if "dogs" == d[i]:
        x+=1
    elif "cats" == d[i]:
        xx+=1
if x > xx:
    print("dogs")
elif x < xx:
    print('cats')
elif x == xx:
    print("equal")
