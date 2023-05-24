import calendar
#import locale

#locale.setlocale(locale.LC_ALL, "en")
#locale.setlocale(locale.LC_ALL, "ru")

year = int(input("Введите год: "))
d = {}
for m in range(1, 13):
    m_range = calendar.monthrange(year, m)
    for i in range(1, m_range[1] + 1):
        w = calendar.weekday(year, m, i)
        d[w] = d.get(w, 0) + 1
print(d)