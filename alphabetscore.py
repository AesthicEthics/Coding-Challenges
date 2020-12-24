a = list((input()))
e = []
c = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(a)):
    d = (c.index(a[i]) + 1)
    e.append(d)
print(sum(e))
