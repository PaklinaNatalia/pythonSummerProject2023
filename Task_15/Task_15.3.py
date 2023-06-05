import re

def phone_num(s):
    regex = r"\+7\((?:812|921)\)\d{3}\-\d{2}[-]?\d{2}"
    return re.findall(regex, s)

print(*phone_num(input("Введите номера телефонов: ")))