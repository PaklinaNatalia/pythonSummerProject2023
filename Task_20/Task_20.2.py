import pandas as pd

lst = []
df = pd.DataFrame([["aaa", 95, 43, "15", 15], [65, "b", "35a", 27, "one"]])
print(df)
sum = 0
for i in df.index:
    for j in df.columns:
        try:
            sum += df.loc[i, j]
        except:
            pass
print(f"Сумма всех чисел = {sum}")
print()
for k in df.index:
    for l in df.columns:
        print(f"{df.loc[k, l]}: {type(df.loc[k, l])}")