"""
You have a list of unique numbers each no larger than 1000. The size of the list is no greater than 50. You perform the following operation on the list repeatedly: 
take the minimum of the numbers, and remove it from the list. You stop when the list is empty.

In what order are the numbers removed?
"""
a = int(input())
b = [int(input()) for b in range(a)]
b.sort()
for i in range(0,len(b)):
    print(b[i])
