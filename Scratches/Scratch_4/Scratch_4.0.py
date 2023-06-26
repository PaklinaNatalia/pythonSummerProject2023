import pandas as pd
df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [3, 4, 5, 6]})
df.index = [100, 200, 300, 400]
print(df)
print()
#print(df[df["a"].isin([1, 3])])
print(df[df["a"] > 2])

import pandas as pd
a = {"Год":[2020, 2021, 2022, 2023], "Кол-во":[15, 20, 5, 32]}
df_1 = pd.DataFrame(a)
print(df_1)
print()
b = {"Цена": [200, 300, 400, 500], "Стоимость": [3000, 6000, 2000, 16000]}
df_2 = pd.DataFrame(b)
print(df_2)
print()
df = df_1.join(df_2)
print(df)

import keyword
key_lst = keyword.kwlist
s = input("Введите текст: ").split()
for n, i in enumerate(s):
    if i in key_lst:
        i = "kw"
        s[n] = i
print(s)

s = list(map(int, input("Введите числа: ").split()))