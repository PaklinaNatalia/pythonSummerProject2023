x = float(input("Введите x: "))
y = float(input("Введите y: "))
if y == 0:
    print("Ошибка! Деление на ноль невозможно.")
    exit()
sum_xy = x + y
diff_xy = x - y
multi_xy = x * y
div_xy = x / y
intdiv_xy = x // y
print(f"x + y = {sum_xy}")
print(f"x - y = {diff_xy}")
print(f"x * y = {multi_xy}")
print(f"x / y = {div_xy}")
print(f"x // y = {intdiv_xy}")
list_xy = [sum_xy, diff_xy, multi_xy, div_xy, intdiv_xy]
list_xy.sort()
if list_xy[-1] == list_xy[-2]:
    print(f"Второе по величине число: {list_xy[-3]}")
else:
    print(f"Второе по величине число: {list_xy[-2]}")