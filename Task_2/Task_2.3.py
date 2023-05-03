fn = 1
n = int(input("Введите n: "))
if n <= 0:
    print("Этот калькулятор умеет считать факториал только от положительных целых чисел.")
    exit()
else:
    for i in range (2, n + 1):
        fn *= i
print(f"n! = {fn}")