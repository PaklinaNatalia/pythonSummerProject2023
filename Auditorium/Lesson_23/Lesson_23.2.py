import psycopg2
con = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    password = "Antaris7",
    host = "127.0.0.1",
    port = "5432"
)
cur = con.cursor()
cur.execute("SELECT admission, name, age, course, department from student")
rows = cur.fetchall()
for row in rows:
    print("admission =", row[0])
    print("name =", row[1])
    print("age =", row[2])
    print("course =", row[3])
    print("department =", row[4], "\n")
con.close()