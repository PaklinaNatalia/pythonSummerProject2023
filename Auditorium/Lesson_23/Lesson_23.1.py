import psycopg2
con = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    password = "Antaris7",
    host = "127.0.0.1",
    port = "5432"
)
cur = con.cursor()
cur.execute('''INSERT INTO student
(admission, name, age, course, department)
VALUES (3423, 'Anthony', 18, 'Electrical Engineering', 'Engineering')''')
con.commit()
con.close()