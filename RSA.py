"""
Problem: 

When a credit card number is sent through the Internet it must be protected so that other people cannot see it. Many web browsers use a protection based on "RSA Numbers."

A number is an RSA number if it has exactly four divisors. In other words, there are exactly four numbers that divide into it evenly. For example, 10 is an RSA number
because it has exactly four divisors (1,2,5,10). 12 is not an RSA number because it has too many divisors (1,2,3,4,6,12). 11 is not an RSA number either. There is only 
one RSA number in therange 10…12.

Write a program that inputs a range of numbers and then counts how many numbers from that range are RSA numbers. You may assume that the numbers in the range are less 
than 1000.

"""

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
