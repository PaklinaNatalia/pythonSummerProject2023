from functools import cmp_to_key
from random import randint
def f1(x, y):
    i = 2
    while x % i:
        i += 1
    j = 2
    while y % j:
        j += 1
    if i < j:
        return -1
    elif i == j:
        return 0
    else:
        return 1
lst = []
for i in range(1, 10):
   lst.append(randint(0, 1024))
print(lst)
print(sorted(lst, key = cmp_to_key(f1)))