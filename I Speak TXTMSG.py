c = []
while True:
    b = input()
    if b == "CU":
        a = ("see you")
    elif b == ":-)":
        a = ("I'm happy")
    elif b == ";-)":
        a = ("wink")
    elif b == ":-P":
        a = ("stick out my tongue")
    elif b == "(~.~)":
        a = ("sleepy")
    elif b == "TA":
        a = ("totally awesome")
    elif b == "CCC":
        a = ("Canadian Computing Competition")
    elif b == "CUZ":
        a = ("because")
    elif b == "TY":
        a = ("thank-you")
    elif b == "YW":
        a = ("you're welcome")
    elif b == "TTYL":
        a = "talk to you later"
    else:
        a = b
    c.append(a)

    if b == "TTYL":
        break

for i in range(len(c)):
    print(c[i])
