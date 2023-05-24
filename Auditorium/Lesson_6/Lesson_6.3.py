def convert_to_c(temp):
    result = (5 / 9) * (temp - 32)
    return result
def convert_to_f(temp):
    result = (9 / 5) * (temp + 32)
    return result
s = int(input("Введите кол-во градусов: "))
print(convert_to_c(convert_to_f(s)))
print(convert_to_f(convert_to_c(s)))
