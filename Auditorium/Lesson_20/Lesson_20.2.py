import pandas as pd

dct = {"Год": [2019, 2020, 2021, 2022, 2023],
       "Товар": ["A", "B", "C", "D", "E"],
       "Кол-во": [10, 20, 30, 40, 50],
       "Цена": [100, 50, 30, 20, 5]}
df = pd.DataFrame(dct)
df["Стоимость"] = df["Цена"] * df["Кол-во"]
df.index = [10, 20, 30, 40, 50]
print(df)
print()
#df.to_excel("../../Texts/Market.xlsx")
df_1 = df.set_index("Год")
df_1.loc[2018] = ["F", 100, 1, 3000]
print(df_1)
print()
print(df + df)
