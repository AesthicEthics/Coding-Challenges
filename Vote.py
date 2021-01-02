c = int(input())
a = (input())
b = a.count('B')
c = a.count('A')
if b > c:
    print("B")
elif b < c:
    print("A")
else:
    print("Tie")
