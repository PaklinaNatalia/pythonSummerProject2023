from datetime import date
import locale

birt_date = date(1993, 7, 27)
locale.setlocale(locale.LC_ALL, "ru")
print("Название месяца:", birt_date.strftime("%B"))
print("Название дня недели:", birt_date.strftime("%A"))
print("Год:", birt_date.strftime("%Y"))
print("Месяц:", birt_date.strftime("%m"))
print("День:", birt_date.strftime("%d"))
print()
locale.setlocale(locale.LC_ALL, "en")
print("Month name:", birt_date.strftime("%B"))
print("Week name:", birt_date.strftime("%A"))
print("Year:", birt_date.strftime("%Y"))
print("Month:", birt_date.strftime("%m"))
print("Day:", birt_date.strftime("%d"))