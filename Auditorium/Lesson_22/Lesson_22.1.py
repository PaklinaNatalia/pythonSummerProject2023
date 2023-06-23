import pandas as pd
import matplotlib.pyplot as plt
x, y = [], []
for i in range(-10, 10):
    x.append(i)
    y.append(i ** 3)
df = pd.DataFrame({"x": x, "y": y})
df.plot("x", "y", color = "g")
plt.show()