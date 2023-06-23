import pandas as pd
import matplotlib.pyplot as plt
import random

df_1 = pd.DataFrame({"a":[1, 2, 3, 4, 5, 6, 7, 8, 9], "b": [1, 1, 1, 2, 2, 2, 3, 3, 3]})
df_1.plot()
plt.show()

df_2 = pd.DataFrame({"a":[1, 2, 3, 4, 5, 6, 7, 8, 9], "b": [1, 1, 1, 2, 2, 2, 3, 3, 3]})
df_2.plot.bar()
plt.show()

x, y = [], []
for _ in range(5000):
    x.append(random.random())
    y.append(random.random())
df = pd.DataFrame({"x": x, "y": y})
df.plot("x", "y", kind = "scatter", color = "g")
plt.show()