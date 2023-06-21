import pandas as pd
import random
df = pd.DataFrame(columns = ["Год", "Товар", "Кол-во", "Цена"], index = range(20))
x = 0
for i in range(2018, 2023):
    for j in ["A", "B", "C", "D"]:
        k = [10, 20, 30, 40, 50][random.randint(0, 4)]
        m = [100, 50, 30, 20, 5][random.randint(0, 4)]
        df.iloc[x] = [i, j, k, m]
        x += 1
df["Итого"] = df["Кол-во"] * df["Цена"]
#df.index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(df)
print()
#print(df[(df.Итого > 1000) & (df.Цена == 100)])
#print(df.sort_values("Итого", ascending = True).tail(3))
#print(df[["Товар", "Кол-во", "Итого"]].groupby("Товар").sum())
#print(df[df["Итого"] == df["Итого"].max()])
#print(df[1::2])
#print(df[df.Цена < df["Цена"].mean()])
#print(df.groupby("Товар").Итого.sum())
print(df.groupby("Год").Итого.sum().max())