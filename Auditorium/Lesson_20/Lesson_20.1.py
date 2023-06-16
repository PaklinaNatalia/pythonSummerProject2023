import pandas as pd

df_1 = pd.DataFrame([[1, "Jason", "King"], [2, "Gabriel", "Prince"], [3, "Anabella", "Princess"]])
df_1.columns = ["Number", "Name", "Title"]
df_1.index = ["A", "B", "C"]
print(df_1)
print()
df_2 = pd.DataFrame({"Country":["RU", "GB", "USA"], "Square":[17125191, 244820, 9147593]})
print(df_2)
print()
lst = {"First":[1, 2, 3], "Second":[2, 3, 4], "Third":[3, 4, 5]}
df_3 = pd.DataFrame(lst)
df_3["Fourth"] = [4, 5, 6]
df_3["Sum"] = df_3["First"] + df_3["Second"] + df_3["Third"] + df_3["Fourth"]
print(df_3)