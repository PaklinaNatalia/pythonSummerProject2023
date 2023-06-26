import psycopg2
from openpyxl import Workbook
con = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    password = "Antaris7",
    host = "127.0.0.1",
    port = "5432"
)
cur = con.cursor()
cur.execute("SELECT author_name, title, amount, price FROM book INNER JOIN author ON book.author_id = author.author_id WHERE book.amount < 100 ORDER BY book.title")
rows = cur.fetchall()
i = 1
total = 0
for row in rows:
    print(f"{i} {row[0]:>3} {row[0]:>5} {100 - row[2]} {row[3]}")
    total += (100 - row[2]) * row[3]
    i += 1
print(f"ИТОГО: {total}")
con.close()