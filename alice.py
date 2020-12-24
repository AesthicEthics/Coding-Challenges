"""
The school year has just begun, so it's time for Alice to find a suitable boyfriend! Naturally, this process will first require some careful research using a 
convenient online academic source known as Facebook.

Alice is considering G (1≤G≤100) guys, and wants to estimate how well-matched she would be with each of them - in other words, how attractive each of them is.
For each guy, Alice can find N (1≤N≤100) pictures of him on Facebook, the i-th of which has attractiveness Ai (1≤Ai≤100). The guy might be as ugly as his 
least-attractive picture (the one with the smallest attractiveness value), or as hot as his most-attractive picture.

In making her important and complex decision, Alice would like to know the potential range of attractiveness of each of the G potential guys!
"""

a = int((input()))
d = []
for i in range(0,a):
    b = int(input())
    for i in range(0,1):
        c = list(map(int, input().split()))
        d.append(c)
for i in range(len(d)):
    x = d[i]
    y = max(x)
    z = min(x)
    print(z,y)
