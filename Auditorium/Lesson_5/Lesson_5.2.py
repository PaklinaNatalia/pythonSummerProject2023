s = list(map(int, input("Введите строку: ").split()))
d = {}
for i, j in enumerate(s): #i – индекс, j – значение
    d[j] = d.get(j, [])
    d[j].append(i)
print(d)