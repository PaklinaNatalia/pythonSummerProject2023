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
cur.execute("SELECT * FROM book ORDER BY book_id")
rows = cur.fetchall()
for row in rows:
    print(row)
print(cur.description)
wb = Workbook()
ws = wb.active
for row in rows:
    ws.append(row)
wb.save("../../Texts/24.0.xlsx")
con.close()