"""
An anagram is a word or a phrase formed by rearranging the letters of another phrase such as ITEM and TIME. Anagrams may be several words long such as CS AT WATERLOO 
and COOL AS WET ART. Note that two phrases may be anagrams of each other even if each phrase has a different number of words (as in the previous example). 
Write a program to determine if two phrases are anagrams of each other.
"""

a = list(str(input()).replace(' ',''))
b = list(str(input()).replace(' ',''))
c = sorted(list(set(a)))
d = sorted(list(set(b)))
if c == d:
    print("Is an anagram.")
else:
    print("Is not an anagram.")
