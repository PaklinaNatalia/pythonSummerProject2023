lst_1 = []
lst_2 = []
n = int(input("Введите n: "))
for i in range(n):
    a = int(input("Введите a: "))
    lst_1.append(a)
j = 0
for i in lst_1:
    j += i
    lst_2.append(j)
print(j)
print(*lst_1)
print(*lst_2)