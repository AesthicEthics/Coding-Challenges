"""
Weird! A week into school, Bob has received T (1≤T≤100) texts in a row from some girl he's never seen before, Alice. Obviously, he's promptly checked her out on Facebook,
and likes what he sees! Now, the hard part - he needs to craft some appropriate replies.

Everyone knows that the affection conveyed in a text is measured by the number of hearts it contains - in other words, the number of times it contains the string "<3". 
Bob certainly wants to reciprocate Alice's seemingly romantic feelings, but doesn't want to come off as overly desperate. He's decided that his response to each text
should contain exactly one more heart than the received text. In fact, he doesn't really want to convey any other information, so his reply will consist of only this number
of instancesof the string "<3", separated by single spaces (and with no leading or trailing spaces).

After waiting the appropriate amount of time (he wouldn't want to reply too quickly, after all), it's time to make a good impression on Alice - 
Bob wants to determine the perfect response to each of the T texts!

"""

a = int(input())
c = []
g = []
j = []
for i in range(1, a+1):
    b = input(str())
    d = c.append(b)
for i in range(len(c)):
    a = c[i]
    e = a.count("<3")
    g.append(e)
for i in range(len(g)):
    h = (g[i] + 1)
    j.append(h)
for i in range(0,len(j)):
    k = j[i]
    print("<3 " * (k))
