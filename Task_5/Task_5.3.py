n = int(input("Введите число: "))
a, b = 0, 1
for i in range(n):
    print(b, end = " ")
    c = b
    b = a + b
    a = c
print()