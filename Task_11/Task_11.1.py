import calendar, locale, datetime

#Названия месяцев на русском
locale.setlocale(locale.LC_ALL, "ru")

#Не взяты в расчет исключения (добавочные дни, не являющиеся четвергами), например для 2023 года: 20 мая и 7 декабря
y = int(input("Введите год: "))
for m in range(1, 13):
    c = calendar.monthcalendar(y, m)
    week_1 = c[0]
    week_3 = c[2]
    week_4 = c[3]
    #ЕСЛИ неделя 1 содержит четверг, ТО неделя 3 содержит искомый четверг
    if week_1[calendar.THURSDAY]:
        fd = week_3[calendar.THURSDAY]
    #ИНАЧЕ неделя 4 содержит искомый четверг
    else:
        fd = week_4[calendar.THURSDAY]
    #Вывести на печать в формате Месяц: Дата
    print(f"{calendar.month_name[m]}: {fd}")