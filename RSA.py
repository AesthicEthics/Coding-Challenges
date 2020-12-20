def d(n):
    for i in range(n):
        x = len([i for i in range(1,n+1) if not n % i])
    return x

a = int(input())
b = int(input())
lst = []
for i in range(a,b+1):
    x = d(i)
    x = 4
    if x:
        pass
        lst.append(i)
msg = f'The number of RSA numbers between {(str(a))} and {(str(b))} is {(str(len(lst)))}'
print(msg)
