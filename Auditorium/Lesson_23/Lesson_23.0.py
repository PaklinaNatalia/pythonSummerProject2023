import psycopg2
con = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    password = "Antaris7",
    host = "127.0.0.1",
    port = "5432"
)
cur = con.cursor()
cur.execute('''CREATE TABLE student
(admission int PRIMARY KEY NOT NULL,
name text NOT NULL,
age int NOT NULL,
course char(50),
department char(50));''')
con.commit()
con.close()