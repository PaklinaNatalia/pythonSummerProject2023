#Функция "Подоходный налог"
def income_tax(income, rate):
    return income * rate / 100

i = int(input("Введите доход: "))
r = int(input("Введите ставку: "))
print(f"При ставке {r} подоходный налог равен {income_tax(i, r)}")