import keyword
s = input("Введите текст: ")
for i in keyword.kwlist:
    s = s.replace(i, "<kw>")
print(s)