a = int(input())
b = 0
lst = []
f = {}
lst1 = []
for i in range(1,1000):
    c = str(a + i)
    b = [int(i) for i in c]
    f = map(str,b)
    g = ''.join(f)
    d = len(set(b))
    if(d == len(b)):
        lst.append(g)
        lst1.append(lst[0])
print(lst[0])
