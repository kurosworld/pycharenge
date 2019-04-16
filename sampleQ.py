import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn")
x = np.arange(0, 10, 0.1)
y = np.sin(x)
y2 = np.cos(x)
fig = plt.figure()

ax = fig.add_subplot(1,1,1)
ax.plot(x, y, label="y=sin(x)")
ax.plot(x, y2, label="y=cos(x)")

ax.legend(loc="best")

plt.show()

plt.close()