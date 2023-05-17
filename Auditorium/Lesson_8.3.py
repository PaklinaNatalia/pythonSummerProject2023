# Квадраты чисел [0; n]
n = int(input("Введите n: "))
for x in range(n + 1):
    print((lambda x: x ** 2)(x))