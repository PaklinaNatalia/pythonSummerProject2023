while True:
    try:
        n = int(input("Введите число: "))
    except ValueError:
        print("Введено неверное число! Повторите ввод.")
    except Exception:
        print("Неизвестная ошибка!")
    else:
        print(n)
        break
