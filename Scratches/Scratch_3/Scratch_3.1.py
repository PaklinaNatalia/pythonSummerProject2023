d0 = {}
for n in range(1, 10):
    d0[n] = n ** 2
print(*d0)
print()
d1 = {n: n ** 2 for n in range(1,10)}
print(*d1)
print()
d2 = {n: n ** 2 for n in range(1,10) if n % 2 == 0}
print(*d2)
print()
d3 = {n: n ** 2 for n in range(1,10) if n % 2}
print(*d3)
print()
d4 = {"a":1, "b":2, "c":3, "d":4, "e":5}
print({k:v for k, v in d4.items() if v > 2})
print()
ages = {"Rose":12, "Jason":20, "Kendra":19, "Gabriel": 17, "Alice":20}
print(*[(k, v) for k, v in ages.items() if v == max(ages.values())])
print(*[(k, v) for k, v in ages.items() if v == 20 if k.startswith("A")])