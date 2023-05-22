from functools import cmp_to_key
from random import randint
def xy(x, y):
    if x < y:
        return -1
    elif x == y:
        return 0
    else:
        return 1
lst = []
for i in range(1, 10):
   lst.append(randint(-255, 255))
print(lst)
print(sorted(lst, key = cmp_to_key(xy)))