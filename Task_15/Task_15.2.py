import re

def car_num(s):
    regex = r"\b[ABCEHKMOPTXАВЕКМНОРСТХ]\d{3}[ABCEHKMOPTXАВЕКМНОРСТХ]{2}78|\b[ABCEHKMOPTXАВЕКМНОРСТХ]\d{3}[ABCEHKMOPTXАВЕКМНОРСТХ]{2}178"
    return re.findall(regex, s)

print(car_num(input("Введите номера автомобилей: ")))