salary = []
while True:
    n = int(input("Введите размер зарплаты сотрудника: "))
    if n == 0:
        print("Данные по зарплате всех сотрудников были внесены.")
        break
    salary.append(n)
print(*salary)
if len(salary) == 0:
    print("Ни один из сотрудников не получает зарплату.")
    exit()
mvalue = sum(salary) / len (salary)
print(f"Средняя зарплата сотрудника: {mvalue}")