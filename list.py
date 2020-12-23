a = int(input())
b = [int(input()) for b in range(a)]
b.sort()
for i in range(0,len(b)):
    print(b[i])
