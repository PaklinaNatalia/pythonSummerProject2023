#Подоходный налог
i = int(input("Введите доход: "))
a = 5000000
if i <= a:
    print(f"Налог к уплате: {(lambda x: x * 0.13)(i)}")
else:
    print(f"Налог к уплате: {(lambda x: a * 0.13 + (x - a) * 0.15)(i)}")