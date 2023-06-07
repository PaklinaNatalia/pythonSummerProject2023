import re

x = int(input("Введите x: "))
n = input("Введите строку: ")

num = [int(i) for i in re.findall(r"\d+", n) if int(i) <= x]
print(num)