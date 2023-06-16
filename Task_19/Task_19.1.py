import itertools
s = [50, 100, 200, 500, 1000, 2000, 5000]
tes = set()
for r in range(1, len(s) + 1):
    for i in itertools.combinations(s, r):
        tes.add(sum(i))
print(*sorted(tes))