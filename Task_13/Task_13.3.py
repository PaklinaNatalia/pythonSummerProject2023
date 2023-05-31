#Нечетные числа из списка
def nechet(n):
    odd_numbers = []
    for i in n:
        if i % 2:
            odd_numbers.append(i)
    return odd_numbers

print(*nechet(list(map(int, input("Введите список: ").split()))))