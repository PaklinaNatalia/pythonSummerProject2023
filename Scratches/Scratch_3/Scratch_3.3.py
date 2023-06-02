try:
    raise Exception("Что-то не так...")
except Exception as e:
    print("Спасите! " + str(e))

def f(n):
    for x in range(n):
        yield x ** 2
g = f(10)
while True:
    try:
        print(next(g))
    except StopIteration:
        print("Числа закончились!")
        break

def sumn(n):
    if n == 0:
        return 0
    else:
        return n + sumn(n - 1)
print(sumn(int(input("Введите n: "))))