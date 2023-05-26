import calendar
for i in range(1, 13):
    wd = calendar.monthrange(2023, i)[0]
    date = 15 + (3 - wd) if wd <= 3 else 15 + (10 - wd)
    print(f"{date} – {i}")