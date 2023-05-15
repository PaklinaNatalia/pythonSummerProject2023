#Вложенные функции
def f(n):
    def f1(p):
        return p * p
    def f2(w):
        return w + w
    if n < 10:
        return f1(n)
    else:
        return f2(n)

x = int(input("Введите n: "))
print(f(x))