def hourglass_asterisk(n):
    if n == 0:
        return
    elif n == 1:
        print("*")
    else:
        print("*" * n)
        hourglass_asterisk(n - 1)
        print("*" * n)

hourglass_asterisk(int(input("Введите n: ")))