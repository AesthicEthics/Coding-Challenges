"""
Waterbending is characterized by being fluid and graceful, acting in concert with the environment. Young Avatar Aang is trying to master this unique art with the 
help of his friend Katara. Katara gives Aang three identical jars with equal amounts of water inside to practice on. Seeing how their practice is going so well,
Sokka came over to play a prank. While Aang and Katara are taking a break, Sokka places a fish in one of those jars. Since Aang had just gotten used to the original
weights of the jars, Sokka postulates that the added weight will surely throw him off.

What's more – the larger the fish, the more Aang will be thrown off. However, while Sokka was snickering to himself about how brilliant the prank was, 
he accidentally mixed up the jars. Now, given the weights of the jars, he would like to how much fish weighs so he can know just how much Aang will screw up.
"""
a = int(input())
b = int(input())
c = int(input())
if a == b:
    print((c-a))
if a == c:
    print((b)-(a))
if b == c:
    print((a)-(b))
