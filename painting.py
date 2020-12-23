n, m = (input().split())
a,b = int(n), int(m)
c = [int(input()) for c in range(a)]
f = []
for i in range(len(c)):
    q = c[i]
    for i in range(0,(3*(10**5))):
        if q == ((i)*(2654435761))%(4294967296):
            f.append(i)
            break
t = 0
h = sorted(f, reverse = True)
for i in range(0,b):
    t+=h[i]
print(t)
