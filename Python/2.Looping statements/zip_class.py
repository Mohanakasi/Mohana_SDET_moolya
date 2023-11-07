""" Traversing through 3 iterables simultaneously"""

s1 = "hai"
s2 = "hey"
s3 = "are"
# print(zip(s1, s2))

for item1, item2, item3 in zip(s1, s2, s3):
    print(item1, item2, item3, sep=" - ")

""" different lengths """
s = "hai"
s1 = "hello"

for i1, i2 in zip(s, s1):
    print(i1, i2)
print()
from itertools import zip_longest
for i1, i2 in zip_longest(s, s1, fillvalue="not present"):
    print(i1, i2)
