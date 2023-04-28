a = [1, 2, 3, 'cat', True, False, [100, 101]]
b = a[:]
a[0] = 111
print(*a)
print(*b)

a = [1, 2, 3, 4]
print(*a)
b = list('cat')
print(*b)