a = int(input())
d =[]
for i in range(0,a):
    c = input()
    d.append(c)
x = 0
xx = 0
for i in range(len(d)):
    if "dogs" == d[i]:
        x+=1
    elif "cats" == d[i]:
        xx+=1
if x > xx:
    print("dogs")
elif x < xx:
    print('cats')
elif x == xx:
    print("equal")
