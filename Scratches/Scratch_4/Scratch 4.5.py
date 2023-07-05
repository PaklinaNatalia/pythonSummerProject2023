def item_count(lst):
    count = 0
    for i in lst:
        if type(i) == list:
            count += item_count(i) + 1
        else:
            count += 1
    return count
print(item_count([1, [2, 3], []]))