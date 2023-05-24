import csv

columns = ["Имя", "Фамилия", "Рейтинг"]
data =[["И1", "Ф1", 10], ["И2", "Ф2", 4], ["И3", "Ф3", 2]]

with open("../../Texts/rating.csv", "w", newline ="") as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    for row in data:
        writer.writerow(row)