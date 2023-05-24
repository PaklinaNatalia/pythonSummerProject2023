import csv
with open("../../Texts/text_06.csv") as fi:
    rows = csv.DictReader(fi)
    su = 0
    for row in rows:
        su += int(row["Salary"])
    print(su)