import re

s = input("Введите строку: ")
z = input("Введите подстроку: ")
print(*re.findall(fr"\w+{z}\w+", s))