a = int((input()))
d = []
for i in range(0,a):
    b = int(input())
    for i in range(0,1):
        c = list(map(int, input().split()))
        d.append(c)
for i in range(len(d)):
    x = d[i]
    y = max(x)
    z = min(x)
    print(z,y)
