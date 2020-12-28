a = list(input().strip().replace(' ','').upper())
b = list(input().strip().replace(' ','').upper())
c = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
q = []
for i in b:
    if i not in c: b.remove(i)
d = 0
for i in range(len(b)):
    if d >= len(a):
        d = 0
    e = c.index(b[i]) + c.index(a[d])
    if e > 25:
        e -= 26
    f = c[e]
    q.append(f)
    d+=1

print(''.join(q))
