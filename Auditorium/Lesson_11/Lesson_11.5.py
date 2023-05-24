from itertools import permutations

s = "abcde"
i = int(input("Введите r: "))
for r in range (1, i):
    print(f"{r} – {len(list(permutations(s, r)))}")