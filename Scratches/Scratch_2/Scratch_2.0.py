#Вернуть только четные значения из списка чисел
def chet(x):
    return 1 - x % 2
print(list(filter(chet, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))