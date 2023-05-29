x = list(map(int, input("Введите список: ").split()))
maximum = [k for k, v in enumerate(x) if v == max(x)]
minimum = [k for k, v in enumerate(x) if v == min(x)]
print(minimum, maximum, sep = ", ")