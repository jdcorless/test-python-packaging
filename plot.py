import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 11, 51)
y = np.sin(x)
plt.plot(x, y)
plt.show()