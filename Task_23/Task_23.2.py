import psycopg2, pandas as pd, matplotlib.pyplot as plt
con = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    password = "Antaris7",
    host = "127.0.0.1",
    port = "5432"
)
cur = con.cursor()
cur.execute("SELECT * from book")
col = list(map(lambda x: x[0], cur.description))
val = cur.fetchall()
df = pd.DataFrame(columns = col, data = val, index = [i for i in range(1, len(val) + 1)])
print(df)
#Просмотреть неурезанный результат
df.to_excel("../Texts/test.xlsx")
df["amount"].plot(grid = True, title = "Количество", color = "r")
plt.show()
df["price"].plot(grid = True, title = "Цена", color = "g")
plt.show()
con.close()