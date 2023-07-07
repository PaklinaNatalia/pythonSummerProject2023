a = list(map(int, input("Введите числа: ").split()))
count = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            count += 1
            print(f"{a[i]}:{a[j]}")
print(f"Количество инверсий в списке {a}: {count}")