print(*[k ** 2 if k % 2 == 0 else k ** 3 for k in range(1, int(input("Введите число: ")) + 1)])
print(*[k ** 2 if k % 2 == 0 else k ** 3 if k % 3 == 0 else k ** 4 for k in range(1, int(input("Введите число: ")) + 1)])
print()

import itertools
for i in itertools.combinations([1, 2, 3, 4, 5], 3):
    print(*i)
print()
for k in itertools.combinations_with_replacement([1, 2, 3, 4, 5], 3):
    print(*k)
print()

while True:
    try:
        n = int(input("Введите число: "))
    except ValueError:
        print("Введено неверное число! Повторите ввод.")
    except Exception:
        print("Неизвестная ошибка!")
    else:
        print(n)
        break
print()

while True:
    fn = input("Введите имя файла: ")
    try:
        f = open(fn)
    except FileNotFoundError:
        print("Файл не найден!")
    else:
        print(f"Файл {fn} найден!")
        break
print()

def fun(n):
    for x in range(n):
        yield x ** 2
g = fun(int(input("Введите n: ")))
for k in g:
    print(k)