i = int(input("Введите i: "))
if (q := i * i) > 3:
    print("Да")
else:
    print("Нет")
print(q)
print()
tes = set(map(int, input("Введите строку чисел: ").split()))
print(sum(tes) / len(tes))
print()
s = input("Введите строку: ")
if len(set(s)) != 33:
    print(False)
else:
    ab = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    print(ab == set(s))