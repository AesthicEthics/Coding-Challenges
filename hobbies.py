a = int(input())
b = input().split()
x = 0
for i in range(len(b)):
    c = len(b[i])
    if c <= 10:
        x+=1
print(x)
