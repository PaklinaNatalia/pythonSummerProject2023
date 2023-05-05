salary = []
while True:
    n = int(input("Введите размер зарплаты сотрудника: "))
    if n == 0:
        print("Ввод окончен.")
        break
    salary.append(n)
print(*salary)
mvalue = sum(salary) / len (salary)
print(f"Средняя зарплата сотрудника: {mvalue}")