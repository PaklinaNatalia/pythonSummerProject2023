#Рисуем треугольник из "+"
n = int(input("Введите n: "))
for i in range(1, n + 1):
    for j in range(i):
        print ('+', end = ' ')
    print()