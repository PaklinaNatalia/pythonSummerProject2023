s = input("Введите строку: ").split()
res = 0
a = int(s[0])
b = int(s[2])
if s[1] == "+":
    res = a + b
elif s[1] == "-":
    res = a - b
elif s[1] == "*":
    res = a * b
elif s[1] == "/":
    res = a / b
else:
    print("Ошибка! Проверьте введенное выражение.")
    exit()
print(f"{s[0]} {s[1]} {s[2]} = {res}")