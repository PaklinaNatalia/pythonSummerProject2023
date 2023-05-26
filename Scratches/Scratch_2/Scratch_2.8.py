s = []
for i in range(10):
    s.append(i ** 3)
print(s)
print()
print(list(map(lambda x: x ** 3, range(10))))
print()
print([x ** 3 for x in range(10)])
print()
print([x for x in range(21) if x % 2 == 0])
print()
origin = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new = [i if i > 0 else 0 for i in origin]
print(origin)
print(new)
print()
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_price = [(lambda x: 0 if x <0 else x)(i) for i in original_prices]
print(new_price)