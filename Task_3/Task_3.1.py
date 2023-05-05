salary = []
while True:
    n = float(input("Введите размер зарплаты сотрудника: "))
    if n == 0:
        print("Данные по зарплате всех сотрудников были внесены.")
        break
    salary.append(n)
if len(salary) == 0:
    print("Ни один из сотрудников не получает зарплату.")
    exit()
else:
    print(*salary)
mvalue = sum(salary) / len (salary)
print(f"Средняя зарплата сотрудника: {mvalue}")