"""
Problem:

You might be surprised to know that 2013 is the first year since 1987 with distinct digits. The years 2013, 2015, 2016, 2017, 2018, 2019 each have distinct digits. 
2012 does not have distinct digits, since the digit 2 is repeated.
Given a year, what is the next year with distinct digits?

"""

a = int(input())
b = 0
lst = []
f = {}
lst1 = []
for i in range(1,1000):
    c = str(a + i)
    b = [int(i) for i in c]
    f = map(str,b)
    g = ''.join(f)
    d = len(set(b))
    if(d == len(b)):
        lst.append(g)
        lst1.append(lst[0])
print(lst[0])
