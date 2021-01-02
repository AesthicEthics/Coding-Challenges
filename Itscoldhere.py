x = []
y = []
for i in range(0,10000):
    a = input().split()
    x.append(a[0])
    y.append(int(a[1]))
    if a[0] == "Waterloo":
        break

h = sorted(y)
i = y.index(h[0])
print(x[i])
