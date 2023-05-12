n = int(input("Введите число: "))
d = {1:1}
for i in range(n + 1):
    x = 1
    for j in range(2, i + 1):
        y = d.get(j, 0)
        d[j] = x+ d.get(j, 0)
        x = y
    for j in range(1, i + 1):
        print(d[j], end = " ")
    print()