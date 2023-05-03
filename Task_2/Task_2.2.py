from random import randint
lst = []
n = int(input("Введите n: "))
if n == 0:
    print("Ноль и есть ноль – нечем заполнять список.")
    exit()
else:
    for i in range(1, 11):
        lst.append(randint(-n, n))
print(lst)
lst.sort()
print(lst)
print(f"Минимальное число: {lst[0]}")