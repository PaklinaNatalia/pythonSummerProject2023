def f(n):
    for x in range(n):
        if x % 2 == 0:
            yield x ** 2
        else:
            yield x ** 3
g = f(int(input("Введите n: ")))
for k in g:
    print(f"{k = }")