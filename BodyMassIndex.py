a = float(input())
b = float(input())
c = (a)/(b*b)
if c > 25.0:
    print("Overweight")
elif c <= 25.0 and c >= 18.5:
    print("Normal weight")
elif c < 18.5:
    print("Underweight"
