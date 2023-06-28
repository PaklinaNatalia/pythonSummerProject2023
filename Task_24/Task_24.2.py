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
cur.execute("CREATE VIEW temp AS (SELECT author_name AS Автор, amount AS Количество FROM author INNER JOIN book ON author.author_id = book.author_id GROUP BY author_name, amount HAVING amount = (SELECT MIN(amount) AS min_amount FROM book))")
rows = cur.fetchall()
for row in rows:
    print(row)
con.close()