from random import randint
lst = [3, -1, 0, 1, 2]
mi = lst[0]
counter = []
for i in lst:
    if mi > i:
        mi = i
        counter = [mi]
    elif mi == i:
        counter.append(mi)
    print(counter)
print(counter)