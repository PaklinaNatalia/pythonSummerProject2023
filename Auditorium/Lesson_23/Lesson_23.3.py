import psycopg2
con = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    password = "Antaris7",
    host = "127.0.0.1",
    port = "5432"
)
cur = con.cursor()
cur.execute("SELECT * FROM book WHERE author_id = 1")
rows = cur.fetchall()
for row in rows:
    print(row)
con.close()