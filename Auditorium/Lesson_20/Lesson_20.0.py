import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 5, num = 50)
y = np.exp(x)

plt.plot(x, y)
plt.grid()
_ = plt.title("y = exp(x)")
plt.show() #Для отображения результата