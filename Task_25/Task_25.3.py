#Одной строкой
#print(input("Введите строку: ").title().replace(" ", ""))
#Функцией как в задании
def camel_style(s):
    res = s.title().replace(" ", "")
    return res
print(camel_style(input("Введите строку: ")))