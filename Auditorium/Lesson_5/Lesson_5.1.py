n = int(input("Введите число: "))
d = {}
for i in range(n):
    s = input("Введите слово: ").split()
    d.setdefault(s[0], s[i])
    d.setdefault(s[i], s[0])
while True:
    q = input("Введите слово: ")
    if q == "stop":
        break
    print(d.get(q, "Нет в словаре"))