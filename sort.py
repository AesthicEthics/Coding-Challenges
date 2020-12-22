"""
Given a list of n numbers, sort them and output them one per line from smallest to largest
"""

a = int(input())
d = []
for i in range(1, a+1):
    b = int(input())
    d.append(b)
d.sort()
for i in range(len(d)):
    print(d[i])
