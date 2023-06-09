import re

s = input("Введите текст: ")
print(re.sub(r"(\b\w+\b)\W+\1", r"\1", s))