a = int(input())
b = int(input())
c = []
d = []
for i in range(a):
    adj = input()
    c.append(adj)

for i in range(b):
    noun = input()
    for i in range(len(c)):
        f = str(str(c[i])+" "+ 'as' +' '+(noun))
        d.append(f)

for i in range(len(d)):
    print(d[i])
