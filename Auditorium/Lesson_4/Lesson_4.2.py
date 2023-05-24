#Число дней в месяце в году
m = {}
for i in [1, 3, 5, 7, 8, 10, 12]:
    m[i] = 31
for i in [4, 6, 9, 11]:
    m[i] = 30
m[2] = 28
while True:
    year = int(input("Год: "))
    month = int(input("Месяц: "))
    if year == 0 and month == 0:
        break
    if year % 4 == 0 and month == 2:
        print(29)
    else:
        print(m[month])