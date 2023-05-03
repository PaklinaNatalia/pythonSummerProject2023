from random import randint
lst = []
n = int(input("Введите n: "))
if n == 0:
    print("Ноль и есть ноль – нечем заполнять список.")
    exit()
elif n < 0:
    for i in range(1, 11):
        lst.append(randint(n, 1))
else:
    for i in range(1, 11):
        lst.append(randint(1, n))
print(lst)
lst.sort()
print(lst)
print(f"Минимальное число: {lst[0]}")