n = int(input("Введите n: "))
for i in range(2, n):
    if n % i == 0:
        print("Составное")
        break
else:
    print("Простое")