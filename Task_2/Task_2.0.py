n = int(input("Введите n: "))
if n == 0:
    print("Умножение на 0 любого числа дает 0.")
    exit()
x = int(input("Введите x: "))
for i in range (1, x+1):
    print (f"{i}*{n} = {n * i}")