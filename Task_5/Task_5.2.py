n = int(input("Введите число: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end = " ")
print()
n = int(input("Введите число: "))
for i in range(2, n + 1):
    hm = 0
    while n % i == 0:
        hm += 1
        n //= i
    if hm:
        print(f"{i = } {hm = }")
    if n == 1:
        break