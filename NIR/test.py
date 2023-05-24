import csv
with open("Excels/user_quiz_result.csv", "r", newline ="") as f1:
    r = csv.DictReader(f1)
    for row in r:
        print(row)