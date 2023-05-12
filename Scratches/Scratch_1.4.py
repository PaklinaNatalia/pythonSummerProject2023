i = int(input("Введите i: "))
if (q := i * i) > 3:
    print("Да")
else:
    print("Нет")
print(q)

tes = set(map(int, input("Введите строку чисел: ").split()))
print(sum(tes) / len(tes))