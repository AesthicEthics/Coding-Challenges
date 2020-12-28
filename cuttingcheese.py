a = list(input().split())
c = []
q = []
for i in range(int(a[0])):
    b = (input().split())
    g = int(b[0])
    f = int(b[1])
    c.append(g)
    q.append(f)
q = sorted(q)
c = sorted(c)
l = 0
x = int(a[0]) - int(a[1])
for i in range(int(a[1])):
    l+=q[i]
if x == 0:
    print(l)
else:
    for i in range(0,x):
        l+=c[i]
print(l)
