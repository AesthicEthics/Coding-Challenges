a = int(input())
x = 0
y = 0
for i in range(a):
  b = list((input()).replace(' ', ''))
  for i in range(len(b)):
    if b[i] == "s" or b[i] == "S":
      x += 1
    if b[i] == "t" or b[i] == "T":
      y += 1
if y > x :
  print("English")
if x > y:
  print("French")
if x == y:
  print("French")
