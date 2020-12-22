a = int(input())
c = []
g = []
j = []
for i in range(1, a+1):
    b = input(str())
    d = c.append(b)
for i in range(len(c)):
    a = c[i]
    e = a.count("<3")
    g.append(e)
for i in range(len(g)):
    h = (g[i] + 1)
    j.append(h)
for i in range(0,len(j)):
    k = j[i]
    print("<3 " * (k))
