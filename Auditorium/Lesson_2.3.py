a = [1, 2, 3, 'cat', True, False, [100, 101]]
b = a[:]
a[0] = 111
print(*a)
print(*b)
print()
a = [1, 2, 3, 4]
print(*a)
b = list('cat')
print(*b)
print()
mass = [1, 2, 3, 4]
print(len(mass))
print(len('cat'))
print()
a = [10, 20, 30, 40]
for k, v in enumerate(a):
    print(k, v)
print()
print(*list(range(10)))