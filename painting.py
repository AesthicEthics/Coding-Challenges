"""
After being trapped and tormented inside of hewmatt10's basement "Art Academy", astrocat879 decided that it was finally time for him to plan an escape. 
Fortunately, hewmatt10 had never actually considered the possibility of him wanting to escape, so the actual escape would be a piece of cake.

Along the Academy, there are a total of N paintings spread across the area, each with a value of vi. Since astrocat879 is short on money, he 
plans to steal some of the paintings while making his escape. However, because hewmatt10 is insecure, all of his paintings' values have been hashed, 
meaning that the value that astrocat879 sees them at is NOT the actual value. Specifically, the paintings' values have been hashed using the following function:

hash(i)=i×2654435761mod232

(hash(i) represents the hashed value, while i represents the original value. It is guaranteed that all integer values of i under 232 will be given a unique hash value.)

astrocat879 doesn't have the time to figure out the original value of the paintings, and so has asked YOU to create a program for him, that will to maximize his profits. 
More specifically, he would like you to sum up the M paintings with the greatest original value.
"""

n, m = (input().split())
a,b = int(n), int(m)
c = [int(input()) for c in range(a)]
f = []
for i in range(len(c)):
    q = c[i]
    for i in range(0,(2*32))):
        if q == ((i)*(2654435761))%(4294967296):
            f.append(i)
            break
t = 0
h = sorted(f, reverse = True)
for i in range(0,b):
    t+=h[i]
print(t)
