"""
At Chip's Fast Food emporium there is a very simple menu. Each food item is selected by entering a digit choice.

Here are the three burger choices:
1 – Cheeseburger (461 Calories)
2 – Fish Burger (431 Calories)
3 – Veggie Burger (420 Calories)
4 – no burger	Here are the three drink choices:
1 – Soft Drink (130 Calories)
2 – Orange Juice (160 Calories)
3 – Milk (118 Calories)
4 – no drink
Here are the three side order choices:
1 – Fries (100 Calories)
2 – Baked Potato (57 Calories)
3 – Chef Salad (70 Calories)
4 – no side order	Here are the three dessert choices:
1 – Apple Pie (167 Calories)
2 – Sundae (266 Calories)
3 – Fruit Cup (75 Calories)
4 – no dessert
Write a program that will compute the total Calories of a meal.

"""

a = int(input())
c = int(input())
b = int(input())
d = int(input())

if a == 1:
    q = 461
elif a == 2:
    q = 431
elif a == 3:
    q = 420
elif a == 4:
    q = 0

if b == 1:
    e = 130
elif b == 2:
    e = 160
elif b == 3:
    e = 118
elif b == 4:
    e = 0

if c == 1:
    f = 100
elif c == 2:
    f = 57
elif c == 3:
    f = 70
elif c == 4:
    f = 0

if d == 1:
    h = 167
elif d == 2:
    h = 266
elif d == 3:
    h = 75
elif d == 4:
    h = 0



print("Your total Calorie count is" + ' ' +  str((q)+(e)+(f)+(h)) +".")
