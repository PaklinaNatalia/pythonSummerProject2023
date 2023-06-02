def count_digits(n):
    if n <= 0:
        return("Введенное n не является натуральным числом!")
    elif n < 10:
        return 1
    else:
        return 1 + count_digits(n/10)

try:
    print(count_digits(int(input("Введите n: "))))
except ValueError:
    print("Некорректное значение!")