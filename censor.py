a = int(input())
c = []
f = []
g = []
for i in range(0,a):
    b = input().split()
    c.append(b)
for i in range(0, len(c)):
    d = c[i]
    for index, item in enumerate(d):
        if len(item) == 4:
            d[index] = "****"
    print(' '.join(d))
