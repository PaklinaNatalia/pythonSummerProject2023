def tax(money, pn = 13):
    res = money * pn / 100
    return res
d = float(input("Введите размер ЗП: "))
print(f"{tax(d) = } ")