s1 = 0
while True:
    n = int(input("Введите n: "))
    if n < 0:
        print("Ввод окончен.")
        break
    s1 += n
print(s1)

s2 = []
while True:
    n = int(input("Введите n: "))
    if n < 0:
        print("Ввод окончен.")
        break
    s2.append(n)
print(s2)