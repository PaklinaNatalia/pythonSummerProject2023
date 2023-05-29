def f(n):
    for x in range(n):
        yield x ** 2
g = f(int(input("Введите n: ")))
for _ in range(10):
    try:
        print(next(g))
    except StopIteration:
        print("Стоп!")
        break
print("Стоп! Стоп!")