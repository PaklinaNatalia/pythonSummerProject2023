d = {}
def fibonacci(n):
    d[n] = d.get(n, 0) + 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(int(input("Введите n: "))))
print(d)