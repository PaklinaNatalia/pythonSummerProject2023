import itertools

for i in itertools.combinations([1, 2, 3, 4, 5], 3):
    print(*i)
print()
for k in itertools.combinations_with_replacement([1, 2, 3, 4, 5], 3):
    print(*k)