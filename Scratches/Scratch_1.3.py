lst = [10, True, [1, 2], "abccde"]
n = len(lst)
for i in range(-n, n):
    print(i, lst[1])
print()

lst = []
n = int(input("Введите n: "))
for i in range(1, n + 1):
    for _ in range(i):
        lst.append(i)
print(lst)
print([n] * n)
print()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = []
for i in range(26):
    result.append(alphabet[i] * (i + 1))
print(result)
print()