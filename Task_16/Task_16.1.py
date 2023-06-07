import re

s = input("Введите строку: ")
print(re.sub(r"\b\w+\b", lambda x: x.group().upper()[0], s).replace(" ", ""))
print(re.sub(r"\b\w+\b", lambda x: x.group().upper()[0]+str(x.start()), s).replace(" ", ""))